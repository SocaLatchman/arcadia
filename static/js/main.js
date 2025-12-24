
function loadMenu() {
    const joystick = document.querySelector('#joystick');
    const sidePanel = document.querySelector('#side-panel');
    joystick.addEventListener('click', (e) => {
       e.preventDefault();
       setTimeout(() => {
          sidePanel.classList.toggle('is-active');
       }, 1000) 
       gsap.to('#joystick-knob', {
          duration: 0.5,
          x: 10,
          y: -1,
          ease: "elastic.out(1,0.3)"
       });
 
    })
    closeMenu();
}

function closeMenu(){
  const closeButton = document.querySelector('#close-button');
  const sidePanel = document.querySelector('#side-panel');
  closeButton.addEventListener('click', (e) => {
      e.preventDefault();
      sidePanel.classList.toggle('is-active');
        gsap.to('#joystick-knob', {
          duration: 0.5,
          x: 0,
          y: 0,
          ease: "elastic.out(1,0.3)"
       });
  })
}





loadMenu();


