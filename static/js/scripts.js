window.onload = () => {

	let table = document.querySelector('table');

	let mainButton = document.querySelector('.main-btn');

	let historyButton = document.querySelector('.history-btn');

	mainButton.onclick = function () {

		let languageList = ['python', 'javascript', 'ruby', 'java', 'c'];

		for (let i = 0; i < languageList.length; i++) {

			fetchGitHub(languageList[i], table);
		}
	};

	historyButton.onclick = () => {

		fetchDB(table);
	};
};

function fetchGitHub(language, table) {

	let url = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=stars&order=desc';

	console.log("Fetching: " + url);

	fetch(url)

		.then((response) => {

			return response.json();
		})

		.then((response) => {

			let item = response.items[0];
			let itemDate = new Date();
			item.date = itemDate.toDateString();

			// POST request to back-end to store information in db
			const xhr = new XMLHttpRequest();
			const url = '/data';
			xhr.open('POST', url, true);
			xhr.setRequestHeader("Content-Type", "application/json");
			xhr.send(JSON.stringify(item));

			xhr.onreadystatechange = () => {

				if (xhr.readyState == 4) {

					console.log(xhr.response)
				}
			};

			// Add item information to HTML
			addTableItem(item, table);

			table.classList.remove("invisible");
		});
}

function addTableItem(item, table) {

	let newRow = table.querySelector('tbody').insertRow();

	let nameButton = document.createElement('button');
	nameButton.setAttribute('type', 'button');
	nameButton.classList.add('btn');
	nameButton.classList.add('btn-primary');
	nameButton.setAttribute('data-toggle', 'modal');
	nameButton.setAttribute('data-target', '#detailsModal');
	nameButton.textContent = item.name;

	let nameCell = newRow.insertCell();
	nameCell.appendChild(nameButton);
	nameCell.onclick = () => {

		document.querySelector('.modal-title').innerHTML = item.name;
		document.querySelector('.modal-body').innerHTML = item.description + '<br><br><a href="' + item.html_url + '">' + item.html_url + '</a>';
	};

	let languageCell = newRow.insertCell();
	languageCell.innerHTML = item.language;

	let starsCell = newRow.insertCell();
	starsCell.innerHTML = item.stargazers_count;

	let forksCell = newRow.insertCell();
	forksCell.innerHTML = item.forks_count;

	let dateCell = newRow.insertCell();
	dateCell.innerHTML = item.date;
}

function fetchDB(table) {

	const xhr = new XMLHttpRequest();
	const url = '/data';
	xhr.open('GET', url, true);
	xhr.send();

	xhr.onreadystatechange = () => {

		if (xhr.readyState == 4) {

			console.log(xhr.response);

			/* for (let i = 0; i < response.length; i++) {

				addTableItem(response[i], table);
			} */
		}
	};
}