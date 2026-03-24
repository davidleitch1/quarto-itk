// battery-viz.js - Modified version using more compatible libraries

// battery-viz.js - Modified version using Canvas with GW/GWh only and no chart title

// This will execute once the slide is loaded
window.addEventListener('load', function() {
    console.log('Battery visualization script loading...');
    const container = document.getElementById('battery-visualization');
    
    if (!container) {
      console.error('Container #battery-visualization not found!');
      return;
    }
    
    // Show loading message
    container.innerHTML = '<div style="color: white; text-align: center; padding: 20px;">' +
      '<h3>Loading Visualization...</h3>' +
      '<p>Please wait while we load the visualization components.</p>' +
      '</div>';
    
    // Render the canvas chart directly
    renderCanvasChart(container);
  });
  
  // Function to render a canvas chart
  function renderCanvasChart(container) {
    // Create canvas element
    container.innerHTML = '<canvas id="battery-chart" width="800" height="400"></canvas>' +
      '<div id="chart-controls" style="text-align: center; margin-top: 10px;"></div>' +
      '<div id="chart-summary" style="margin-top: 15px;"></div>';
    
    const canvas = document.getElementById('battery-chart');
    const ctx = canvas.getContext('2d');
    const controlsDiv = document.getElementById('chart-controls');
    const summaryDiv = document.getElementById('chart-summary');
    
    // Set up data
    const powerData = [
      { state: 'NSW', commissioning: 850, construction: 2150, operating: 406, cis: 250 },
      { state: 'QLD', commissioning: 200, construction: 3019, operating: 606, cis: 300 },
      { state: 'SA', commissioning: 185, construction: 566, operating: 549, cis: 0 },
      { state: 'VIC', commissioning: 0, construction: 1553, operating: 741, cis: 599 }
    ];
    
    const energyData = [
      { state: 'NSW', commissioning: 1679, construction: 6833, operating: 700, cis: 904 },
      { state: 'QLD', commissioning: 400, construction: 7702, operating: 1144, cis: 1200 },
      { state: 'SA', commissioning: 370, construction: 1694, operating: 572, cis: 0 },
      { state: 'VIC', commissioning: 0, construction: 4292, operating: 1141, cis: 1690 }
    ];
    
    // Calculate NEM totals for power
    const nemPower = {
      commissioning: powerData.reduce((sum, state) => sum + (state.commissioning || 0), 0),
      construction: powerData.reduce((sum, state) => sum + (state.construction || 0), 0),
      operating: powerData.reduce((sum, state) => sum + (state.operating || 0), 0),
      cis: powerData.reduce((sum, state) => sum + (state.cis || 0), 0)
    };
    
    // Calculate NEM totals for energy
    const nemEnergy = {
      commissioning: energyData.reduce((sum, state) => sum + (state.commissioning || 0), 0),
      construction: energyData.reduce((sum, state) => sum + (state.construction || 0), 0),
      operating: energyData.reduce((sum, state) => sum + (state.operating || 0), 0),
      cis: energyData.reduce((sum, state) => sum + (state.cis || 0), 0)
    };
    
    // Add NEM totals to data
    powerData.push({ state: 'NEM', ...nemPower });
    energyData.push({ state: 'NEM', ...nemEnergy });
    
    // Dracula theme colors
    const colors = {
      background: '#282a36',
      currentLine: '#44475a',
      foreground: '#f8f8f2',
      comment: '#6272a4',
      cyan: '#8be9fd',
      green: '#50fa7b',
      orange: '#ffb86c',
      pink: '#ff79c6',
      purple: '#bd93f9',
      red: '#ff5555',
      yellow: '#f1fa8c'
    };
    
    // Set up state
    let viewMode = 'power';
    
    // Function to convert to GW/GWh
    function convertValue(value) {
      if (!value) return 0;
      return value / 1000;
    }
    
    function getUnitLabel() {
      return viewMode === 'power' ? 'GW' : 'GWh';
    }
    
    // Create controls - only power/energy toggle
    controlsDiv.innerHTML = `
      <button id="btn-power" style="background-color: ${colors.pink}; color: white; border: none; padding: 5px 10px; margin-right: 5px; border-radius: 4px; cursor: pointer;">Power (GW)</button>
      <button id="btn-energy" style="background-color: ${colors.currentLine}; color: white; border: none; padding: 5px 10px; margin-right: 15px; border-radius: 4px; cursor: pointer;">Energy (GWh)</button>
    `;
    
    // Add event listeners to buttons
    document.getElementById('btn-power').addEventListener('click', function() {
      viewMode = 'power';
      updateButtonStyles();
      drawChart();
    });
    
    document.getElementById('btn-energy').addEventListener('click', function() {
      viewMode = 'energy';
      updateButtonStyles();
      drawChart();
    });
    
    function updateButtonStyles() {
      document.getElementById('btn-power').style.backgroundColor = viewMode === 'power' ? colors.pink : colors.currentLine;
      document.getElementById('btn-energy').style.backgroundColor = viewMode === 'energy' ? colors.pink : colors.currentLine;
    }
    
    // Function to draw the chart
    function drawChart() {
      // Clear canvas
      ctx.fillStyle = colors.background;
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      // Set up data for current view
      const data = viewMode === 'power' ? powerData : energyData;
      const barWidth = 120;
      const barSpacing = 40;
      const marginLeft = 50;
      const marginBottom = 50;
      const marginTop = 30; // Reduced top margin since we removed the title
      const maxHeight = canvas.height - marginBottom - marginTop;
      
      // Get max value for scaling
      let maxValue = 0;
      data.forEach(state => {
        const total = state.operating + state.commissioning + state.construction + state.cis;
        if (total > maxValue) maxValue = total;
      });
      
      // Scale factor (always in GW/GWh)
      const scale = maxHeight / (maxValue / 1000);
      
      // Draw axes
      ctx.strokeStyle = colors.foreground;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(marginLeft, marginTop);
      ctx.lineTo(marginLeft, canvas.height - marginBottom);
      ctx.lineTo(canvas.width - marginLeft, canvas.height - marginBottom);
      ctx.stroke();
      
      // Draw y-axis labels
      ctx.fillStyle = colors.foreground;
      ctx.font = '12px Arial';
      ctx.textAlign = 'right';
      for (let i = 0; i <= 5; i++) {
        const y = marginTop + (maxHeight * (1 - i / 5));
        const value = ((maxValue / 1000) * i / 5).toFixed(1);
        ctx.fillText(value.toString(), marginLeft - 5, y + 4);
      }
      
      // Draw unit label
      ctx.save();
      ctx.translate(15, canvas.height / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.textAlign = 'center';
      ctx.fillText(getUnitLabel(), 0, 0);
      ctx.restore();
      
      // Draw bars
      let x = marginLeft + 40;
      data.forEach((state, index) => {
        // Skip NEM for now
        if (state.state !== 'NEM' || index === data.length - 1) {
          // Draw stacked bar
          let y = canvas.height - marginBottom;
          
          // Operating
          const operatingHeight = convertValue(state.operating) * scale;
          ctx.fillStyle = colors.green;
          ctx.fillRect(x, y - operatingHeight, barWidth, operatingHeight);
          y -= operatingHeight;
          
          // Commissioning
          const commissioningHeight = convertValue(state.commissioning) * scale;
          ctx.fillStyle = colors.yellow;
          ctx.fillRect(x, y - commissioningHeight, barWidth, commissioningHeight);
          y -= commissioningHeight;
          
          // Construction
          const constructionHeight = convertValue(state.construction) * scale;
          ctx.fillStyle = colors.orange;
          ctx.fillRect(x, y - constructionHeight, barWidth, constructionHeight);
          y -= constructionHeight;
          
          // CIS
          const cisHeight = convertValue(state.cis) * scale;
          ctx.fillStyle = colors.cyan;
          ctx.fillRect(x, y - cisHeight, barWidth, cisHeight);
          
          // Draw label
          ctx.fillStyle = colors.foreground;
          ctx.textAlign = 'center';
          ctx.fillText(state.state === 'NEM' ? 'NEM (Total)' : state.state, x + barWidth / 2, canvas.height - marginBottom + 20);
          
          x += barWidth + barSpacing;
        }
      });
      
      // Draw legend
      const legendX = marginLeft;
      const legendY = marginTop / 2 + 10; // Adjusted for no title
      const legendSpacing = 100;
      
      ctx.fillStyle = colors.green;
      ctx.fillRect(legendX, legendY - 8, 15, 15);
      ctx.fillStyle = colors.foreground;
      ctx.textAlign = 'left';
      ctx.fillText('Operating', legendX + 20, legendY);
      
      ctx.fillStyle = colors.yellow;
      ctx.fillRect(legendX + legendSpacing, legendY - 8, 15, 15);
      ctx.fillStyle = colors.foreground;
      ctx.fillText('Commissioning', legendX + legendSpacing + 20, legendY);
      
      ctx.fillStyle = colors.orange;
      ctx.fillRect(legendX + legendSpacing * 2, legendY - 8, 15, 15);
      ctx.fillStyle = colors.foreground;
      ctx.fillText('Construction', legendX + legendSpacing * 2 + 20, legendY);
      
      ctx.fillStyle = colors.cyan;
      ctx.fillRect(legendX + legendSpacing * 3, legendY - 8, 15, 15);
      ctx.fillStyle = colors.foreground;
      ctx.fillText('CIS', legendX + legendSpacing * 3 + 20, legendY);
      
      // Update summary
      updateSummary();
    }
    
    function updateSummary() {
      const currentData = viewMode === 'power' ? powerData : energyData;
      const nem = currentData.find(d => d.state === 'NEM');
      const totalValue = nem.operating + nem.commissioning + nem.construction + nem.cis;
      
      // Find largest state (excluding NEM)
      let largestState = '';
      let largestValue = 0;
      currentData.forEach(state => {
        if (state.state !== 'NEM') {
          const total = state.operating + state.commissioning + state.construction + state.cis;
          if (total > largestValue) {
            largestValue = total;
            largestState = state.state;
          }
        }
      });
      
      // Calculate percentages
      const operatingPercent = Math.round((nem.operating / totalValue) * 100);
      const commissioningPercent = Math.round((nem.commissioning / totalValue) * 100);
      const constructionPercent = Math.round((nem.construction / totalValue) * 100);
      const cisPercent = Math.round((nem.cis / totalValue) * 100);
      
      // Display summary with values in GW/GWh
      summaryDiv.innerHTML = `
        <div style="display: flex; justify-content: space-between; background-color: ${colors.currentLine}; padding: 10px; border-radius: 8px; color: ${colors.foreground}; font-size: 12px;">
          <div>
            <h4 style="color: ${colors.purple}; margin: 0 0 5px 0;">NEM Summary</h4>
            <p style="margin: 2px 0;">
              <span style="color: ${colors.pink};">Total ${viewMode === 'power' ? 'Power' : 'Energy'}:</span> 
              ${convertValue(totalValue).toFixed(1)} ${getUnitLabel()}
            </p>
            <p style="margin: 2px 0;">
              <span style="color: ${colors.yellow};">Largest State:</span> ${largestState}
            </p>
          </div>
          
          <div>
            <h4 style="color: ${colors.purple}; margin: 0 0 5px 0;">Phase Breakdown</h4>
            <p style="margin: 2px 0;">
              <span style="color: ${colors.green};">Operating:</span> 
              ${convertValue(nem.operating).toFixed(1)} ${getUnitLabel()} (${operatingPercent}%)
            </p>
            <p style="margin: 2px 0;">
              <span style="color: ${colors.yellow};">Commissioning:</span> 
              ${convertValue(nem.commissioning).toFixed(1)} ${getUnitLabel()} (${commissioningPercent}%)
            </p>
          </div>
          
          <div>
            <p style="margin: 18px 0 2px 0;">
              <span style="color: ${colors.orange};">Construction:</span> 
              ${convertValue(nem.construction).toFixed(1)} ${getUnitLabel()} (${constructionPercent}%)
            </p>
            <p style="margin: 2px 0;">
              <span style="color: ${colors.cyan};">CIS:</span> 
              ${convertValue(nem.cis).toFixed(1)} ${getUnitLabel()} (${cisPercent}%)
            </p>
          </div>
        </div>
      `;
    }
    
    // Initial draw
    drawChart();
  }