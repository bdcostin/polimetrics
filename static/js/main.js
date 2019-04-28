
var $ = require('jQuery')
var ScrollMagic = require('ScrollMagic')

$(document).ready(function () {
  var controller = new ScrollMagic.Controller()
  var ourScene = new ScrollMagic.Scene({
    triggerElement: '#project01'

  })
    .setClassToggle('#project01', 'fade-in')

    .addTo(controller)
  var controller = new ScrollMagic.Controller()
  var ourScene = new ScrollMagic.Scene({
    triggerElement: '#project02'

  })
    .setClassToggle('#project02', 'fade-in')
    .addTo(controller)

  var controller = new ScrollMagic.Controller()
  var ourScene = new ScrollMagic.Scene({
    triggerElement: '#project03'

  })
    .setClassToggle('#project03', 'fade-in')
    .addTo(controller)

  var controller = new ScrollMagic.Controller()
  var ourScene = new ScrollMagic.Scene({
    triggerElement: '#project04'

  })
    .setClassToggle('#project04', 'fade-in')
    .addTo(controller)

  var controller = new ScrollMagic.Controller()
  var ourScene = new ScrollMagic.Scene({
    triggerElement: '#navel'

  })
    .setClassToggle('#navbar', 'fade-in')
    .addTo(controller)
})

let deadline = new Date(`feb 3, 2020 00:01:00`).getTime()

let x = setInterval(function () {
  let now = new Date().getTime()
  let t = deadline - now
  let days = Math.floor(t / (1000 * 60 * 60 * 24))
  let hours = Math.floor((t % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  let minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60))
  let seconds = Math.floor((t % (1000 * 60)) / 1000)
  document.getElementById('day').innerHTML = days
  document.getElementById('hour').innerHTML = hours
  document.getElementById('minute').innerHTML = minutes
  document.getElementById('second').innerHTML = seconds
  if (t < 0) {
    clearInterval(x)
    document.getElementById('day').innerHTML = '0'
    document.getElementById('hour').innerHTML = '0'
    document.getElementById('minute').innerHTML = '0'
    document.getElementById('second').innerHTML = '0'
  }
}, 1000)

document.addEventListener('DOMContentLoaded', function () {
  let acc = document.getElementsByClassName('accordion')
  let i

  for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener('click', function () {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
      this.classList.toggle('active')

      /* Toggle between hiding and showing the active panel */
      let panel = this.nextElementSibling
      if (panel.style.display === 'block') {
        panel.style.display = 'none'
      } else {
        panel.style.display = 'block'
      }
    })
  }
})

document.addEventListener('DOMContentLoaded', function () {
  let acc = document.getElementsByClassName('accordion')
  let i

  for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener('click', function () {
      this.classList.toggle('active')
      let panel = this.nextElementSibling
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null
      } else {
        panel.style.maxHeight = panel.scrollHeight + 'px'
      }
    })
  }
})
