function authorisation(login, password)
{
	var xhr = new XMLHttpRequest();
	var params = 'login=' + encodeURIComponent(login) +'&password=' + encodeURIComponent(password);


	 xhr.open("POST", 'http://127.0.0.1:8000/signin?', true);
	 xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	 xhr.send(params);
	 	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else {
			getJson = xhr.responseText;
			const obj = JSON.parse(getJson);
			console.log(obj["status"]);
			if (obj["status"] == true){
				document.location = "menu";
			}
			alert(xhr.responseText);
		}
	}
	return false;
}
function enter()
{
	let login = document.querySelectorAll("#login_input > input");
	let password = document.querySelectorAll("#password_input > input");

//	console.log(login[0].value, password);


	if (login[0].value == "" || password[0].value == "")
		document.location="main";
	else
	{
		console.log("else");
		if (authorisation(login[0].value, password[0].value) == true)
		{
			console.log("auth");
			document.location = "menu";
		}
	}
}

function send_registration_data(email, password)
{
	alert("send" + email + " " + password);
	var xhr = new XMLHttpRequest();
	var params = 'email=' + encodeURIComponent(email) +'&password=' + encodeURIComponent(password);


	xhr.open("POST", 'http://127.0.0.1:8000/registrationRe?', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(params);

 	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else {
			getJson = xhr.responseText;
			const obj = JSON.parse(getJson);
			console.log(obj["status"]);
			if (obj["status"] == true){
				alert("Письмо с подтверждением отправлено на вашу почту");
				document.location = "main";
			}
		}
	}
}

function send_profile_data()
{
	let lastname = document.querySelectorAll("#lastname > input");
	let firstname = document.querySelectorAll("#firstname > input");
	let secondname = document.querySelectorAll("#secondname > input");
	let nickname = document.querySelectorAll("#nickname > input");
	let datebirth = document.querySelectorAll("#birthdate > input");
	let school = document.querySelectorAll("#school > input");
	let form = document.querySelectorAll("#form > input");

	var xhr = new XMLHttpRequest();
	var params = 'nickname=' + encodeURIComponent(nickname) +'&surname=' + encodeURIComponent(lastname) + "&name=" + encodeURIComponent(firstname) + "&secondname=" + encodeURIComponent(secondname) + "&school=" + encodeURIComponent(school) + "&form=" + encodeURIComponent(form) + "&datebirth=" + encodeURIComponent(datebirth);


	xhr.open("POST", 'http://127.0.0.1:8000/profileData?', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(params);

	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else {
			getJson = xhr.responseText;
			const obj = JSON.parse(getJson);
			console.log(obj["status"]);
			if (obj["status"] == true){
				document.location = "main";
			}
		}
	}
}

function register()
{
	if (document.getElementById("errortext") != null)
		document.body.removeChild(document.getElementById("errortext"));
	if (document.getElementById("errortext2") != null)
		document.body.removeChild(document.getElementById("errortext2"));
	let email = document.querySelectorAll("#email > input")
	let password = document.querySelectorAll("#password > input")
	let password2 = document.querySelectorAll("#password2 > input")
	if (email[0].value == "" || password[0].value == "" || password2[0].value == "")
	{
		let text1 = document.createElement("p");
		text1.innerHTML = "Незаполненные поля";
		text1.setAttribute("id", "errortext")
		text1.setAttribute("class", "note")
		document.body.appendChild(text1);
	}
	else if (password[0].value != password2[0].value)
	{
		let text1 = document.createElement("p");
		text1.innerHTML = "Пароли не совпадают";
		text1.setAttribute("id", "errortext2")
		text1.setAttribute("class", "note")

		document.body.appendChild(text1);
	}
	else if (document.getElementById("infotext") == null)
	{
		let text = document.createElement("p");
		text.innerHTML = "Письмо с подтверждением отправлено на вашу почту";
		text.setAttribute("id", "infotext")
		text.setAttribute("class", "note")

		send_registration_data(email[0].value, password[0].value);
	}
}

function register_save()
{
//	console.log("reg_save");
	if (document.getElementById("errortext") != null)
	{
		document.body.removeChild(document.getElementById("errortext"));
	}
//	console.log("reg continue");
	let fields = document.querySelectorAll("input");
	var flag = new Boolean(true);
	for (var i = 0; i < fields.length; i++)
		if (fields[i].value == "")
			flag = false;
//	console.log(flag);
	if (!flag)
	{
		let text = document.createElement("p");
		text.innerHTML = "Заполните все поля ввода";
		text.setAttribute("id", "errortext");
		text.setAttribute("class", "note");

		document.body.appendChild(text);
	}
	else
	{
		send_profile_data();
	}
}