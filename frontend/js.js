document.addEventListener("DOMContentLoaded", function() {
    const dragItems = document.querySelectorAll(".drag-container li");
    const dropArea = document.getElementById("drop-area");
  
    // Add event listeners for drag events
    dragItems.forEach(function(item) {
      item.addEventListener("dragstart", handleDragStart);
      item.addEventListener("dragend", handleDragEnd);
    });
  
    // Add event listeners for drop events
    dropArea.addEventListener("dragover", handleDragOver);
    dropArea.addEventListener("dragenter", handleDragEnter);
    dropArea.addEventListener("dragleave", handleDragLeave);
    dropArea.addEventListener("drop", handleDrop);
  
    function handleDragStart(event) {
      event.dataTransfer.setData("text/plain", event.target.textContent);
      event.target.classList.add("dragging");
    }
  
    function handleDragEnd(event) {
      event.target.classList.remove("dragging");
    }
  
    function handleDragOver(event) {
      event.preventDefault();
      event.dataTransfer.dropEffect = "move";
    }
  
    function handleDragEnter(event) {
      event.target.classList.add("drag-over");
    }
  
    function handleDragLeave(event) {
      event.target.classList.remove("drag-over");
    }
  
    function handleDrop(event) {
      event.preventDefault();
      event.target.classList.remove("drag-over");
      const questionText = event.dataTransfer.getData("text/plain");
      const question = createQuestionElement(questionText);
      event.target.appendChild(question);
  
      // Change text color of the dropped question
      question.style.color = "#42a5f5";
    }
  
    function createQuestionElement(content) {
      const listItem = document.createElement("li");
      listItem.textContent = content;
      listItem.classList.add("question-list-item");
  
      const removeButton = document.createElement("span");
      removeButton.textContent = "Remove";
      removeButton.classList.add("remove-button");
      removeButton.addEventListener("click", function() {
        listItem.remove();
      });
  
      listItem.appendChild(removeButton);
      return listItem;
    }
    function handleDragEnter(event) {
        event.target.classList.add("drag-over");
      }
      
      function handleDragLeave(event) {
        event.target.classList.remove("drag-over");
      }
      
      function handleDrop(event) {
        event.preventDefault();
        event.target.classList.remove("drag-over");
        const questionText = event.dataTransfer.getData("text/plain");
        const question = createQuestionElement(questionText);
        event.target.appendChild(question);
      
        // Change text color of the dropped question
        question.style.color = "#fff";
        // Generate a random background color for the dropped question
        const randomColor = getRandomColor();
        question.style.backgroundColor = randomColor;
      }
      
      function getRandomColor() {
        const letters = "0123456789ABCDEF";
        let color = "#";
        for (let i = 0; i < 6; i++) {
          color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
      }
      
  });
  