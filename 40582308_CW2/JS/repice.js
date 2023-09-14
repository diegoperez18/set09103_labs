/*Forms*/
function welcomeFunction(){
  alert('Congratulations you have created an account, welcome to the family!');
}

function lostpassFunction() {
  let email = prompt("Please enter your email address");
  if (email != null) {
    document.getElementById("lost").innerHTML =
    "An email has been sent to " + email + " to reset your password" ;
  }
}
/*End -Forms*/

/*Quick & easy*/
function displayPancake()
{document.getElementById("pancake").style.display="block";
document.getElementById("beetroot").style.display="none";
document.getElementById("cannellini").style.display="none";
document.getElementById("calzone").style.display="none";
document.getElementById("kormaveg").style.display="none";
document.getElementById("pesto").style.display="none";
document.getElementById("chickpea").style.display="none";
document.getElementById("tofukebab").style.display="none";
}

function displayBeetroot()
{document.getElementById("pancake").style.display="none";
document.getElementById("beetroot").style.display="block";
document.getElementById("cannellini").style.display="none";
document.getElementById("calzone").style.display="none";
document.getElementById("kormaveg").style.display="none";
document.getElementById("pesto").style.display="none";
document.getElementById("chickpea").style.display="none";
document.getElementById("tofukebab").style.display="none";
}

function displayCannellini()
{document.getElementById("pancake").style.display="none";
document.getElementById("beetroot").style.display="none";
document.getElementById("cannellini").style.display="block";
document.getElementById("calzone").style.display="none";
document.getElementById("kormaveg").style.display="none";
document.getElementById("pesto").style.display="none";
document.getElementById("chickpea").style.display="none";
document.getElementById("tofukebab").style.display="none";
}

function displayCalzone()
{document.getElementById("pancake").style.display="none";
document.getElementById("beetroot").style.display="none";
document.getElementById("cannellini").style.display="none";
document.getElementById("calzone").style.display="block";
document.getElementById("kormaveg").style.display="none";
document.getElementById("pesto").style.display="none";
document.getElementById("chickpea").style.display="none";
document.getElementById("tofukebab").style.display="none";
}

function displayKormaveg()
{document.getElementById("pancake").style.display="none";
document.getElementById("beetroot").style.display="none";
document.getElementById("cannellini").style.display="none";
document.getElementById("calzone").style.display="none";
document.getElementById("kormaveg").style.display="block";
document.getElementById("pesto").style.display="none";
document.getElementById("chickpea").style.display="none";
document.getElementById("tofukebab").style.display="none";
}

function displayPesto()
{document.getElementById("pancake").style.display="none";
document.getElementById("beetroot").style.display="none";
document.getElementById("cannellini").style.display="none";
document.getElementById("calzone").style.display="none";
document.getElementById("kormaveg").style.display="none";
document.getElementById("pesto").style.display="block";
document.getElementById("chickpea").style.display="none";
document.getElementById("tofukebab").style.display="none";
}

function displayChickpea()
{document.getElementById("pancake").style.display="none";
document.getElementById("beetroot").style.display="none";
document.getElementById("cannellini").style.display="none";
document.getElementById("calzone").style.display="none";
document.getElementById("kormaveg").style.display="none";
document.getElementById("pesto").style.display="none";
document.getElementById("chickpea").style.display="block";
document.getElementById("tofukebab").style.display="none";
}

function displayTofukebab()
{document.getElementById("pancake").style.display="none";
document.getElementById("beetroot").style.display="none";
document.getElementById("cannellini").style.display="none";
document.getElementById("calzone").style.display="none";
document.getElementById("kormaveg").style.display="none";
document.getElementById("pesto").style.display="none";
document.getElementById("chickpea").style.display="none";
document.getElementById("tofukebab").style.display="block";
}

/*End - Quick & easy*/

/*Vegetarian*/
function displayCoco(myimage)
{myimage.src="../pictures/coco.png"}

function displayWheat(myimage)
{myimage.src="../pictures/wheat.png"}

function displayLentils(myimage)
{myimage.src="../pictures/lentils.png"}

function displayTofu(myimage)
{myimage.src="../pictures/tofu.png"}

function displayNuts(myimage)
{myimage.src="../pictures/nuts.png"}

function displayBeans(myimage)
{myimage.src="../pictures/greenbeans.png"}

/*End-Vegetarian*/

/*Vegan*/
function displayPestos(myimage)
{myimage.src="../pictures/pesto.png"}

function displayCannellinis(myimage)
{myimage.src="../pictures/cannellini.png"}


function displayPancakes(myimage)
{myimage.src="../pictures/pancake.png"}

function displayCalzones(myimage)
{myimage.src="../pictures/calzone.png"}

/*End-Vegan*/

/*Buy products here*/
function basketFunction(){
  alert('The product was added to your basket!');
}
/*End- Buy products here*/

