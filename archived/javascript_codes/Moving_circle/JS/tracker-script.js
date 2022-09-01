const AREA = document.body;
const CIRCLE1 = document.querySelector('.circle1');
const CIRCLE2 = document.querySelector('.circle2');

var windowWidth = window.innerWidth;
var windowHeight = window.innerHeight;

function mouseCoordinates(e) {
    // Capture the event object (mouse movement).
    // Get X coordinate (distance from left viewport edge) via clientX property.
    // Take total window width, subtract current coordinate and width of circle.
    // Do the same for Y coordinate (distance from top viewport edge).
    var horizontalPosition = e.clientX -26 ;
    var verticalPosition= e.clientY -26;

    // Set horizontal and vertical position.
    CIRCLE1.style.left = horizontalPosition + 'px';
    CIRCLE1.style.top = verticalPosition + 'px';
    CIRCLE2.style.left = windowWidth - horizontalPosition + 'px';
    CIRCLE2.style.top = windowHeight - verticalPosition + 'px';

    if ((horizontalPosition >= windowWidth/2 - 30 && horizontalPosition <= windowWidth/2 + 30) && (verticalPosition >= windowHeight/2 -25 && verticalPosition <= windowHeight/2 + 25)){
      //CIRCLE2.style.backgroundColor = "blue";
      //CIRCLE2.style.borderColor = "blue";
       if (CIRCLE1.style.backgroundColor == "green"){
       CIRCLE2.style.backgroundColor = "green";
       CIRCLE2.style.borderColor = "green";
   }else{
     CIRCLE2.style.backgroundColor = "red";
     CIRCLE2.style.borderColor = "red";
   }
 }
    else{
      CIRCLE2.style.backgroundColor = "orange";
      CIRCLE2.style.borderColor = "orange";
    }
}

function changeColorOnTouch(e) {
  if (CIRCLE1.style.backgroundColor == "green"){
    CIRCLE1.style.backgroundColor = "white";
    CIRCLE1.style.borderColor = "red";
    //CIRCLE.removeAttribute("style")
    console.log("removed : "+e.clientX+","+e.clientY)
  }
  else{
    CIRCLE1.style.backgroundColor = "green";
    CIRCLE1.style.borderColor = "green";
    console.log("added")
  }

}

// When the mouse moves, run the mouseCoordinates function.
AREA.addEventListener('mousemove', mouseCoordinates, false);

// When the mouse touches the circle, run the changeColorOnTouch function.
CIRCLE1.addEventListener('click', changeColorOnTouch, false);

// When the mouse leaves the circle, remove inline styles with an anonymous function.
//CIRCLE.addEventListener('click', function(){CIRCLE.removeAttribute("style");}, false);
