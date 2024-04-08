document.getElementById('next-button').addEventListener('click', function() {
    var currentQuestion = document.querySelector('.question[style="display:block;"]');
    var nextQuestion = currentQuestion.nextElementSibling;
    if (nextQuestion) {
        currentQuestion.style.display = 'none';
        nextQuestion.style.display = 'block';
    } else {
        // Submit form or do something else when all questions are answered
        alert('Toutes les questions ont été répondues. Envoyez le formulaire !');
    }
});