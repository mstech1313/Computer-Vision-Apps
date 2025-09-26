document.addEventListener('DOMContentLoaded', function() {
  const analyzeBtn = document.getElementById('analyzeBtn');
  if (analyzeBtn) {
    analyzeBtn.addEventListener('click', async function() {
      const imageInput = document.getElementById('imageInput');
      const resultDiv = document.getElementById('result');
      if (!imageInput.files || imageInput.files.length === 0) {
        resultDiv.textContent = 'Please select an image.';
        return;
      }
      const formData = new FormData();
      formData.append('image', imageInput.files[0]);
      resultDiv.textContent = 'Analyzing...';
      try {
        const response = await fetch('/api/analyze-image', {
          method: 'POST',
          body: formData
        });
        const data = await response.json();
        resultDiv.textContent = data.description || 'No description found';
      } catch (err) {
        resultDiv.textContent = 'Error analyzing image.';
      }
    });
  }
});
