window.onload = () => {

	let table = document.querySelector('table');

	let button = document.querySelector('button');

	button.onclick = function () {

		let languageList = ['python', 'javascript', 'ruby', 'java', 'c'];

		for (let i = 0; i < languageList.length; i++) {

			FetchNow(languageList[i], table);
		}
	};
};

function FetchNow(language, table) {

	let url = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=stars&order=desc';

	fetch(url)

		.then((response) => {

			return response.json();
		})

		.then((response) => {

			let item = response.items[0];

			// TODO: POST request to back-end to store information in db
			
			let newRow = table.querySelector('tbody').insertRow();

			let nameCell = newRow.insertCell();
			nameCell.innerHTML = item.name;

			let languageCell = newRow.insertCell();
			languageCell.innerHTML = item.language;

			let starsCell = newRow.insertCell();
			starsCell.innerHTML = item.stargazers_count;

			let forksCell = newRow.insertCell();
			forksCell.innerHTML = item.forks_count;

			let dateCell = newRow.insertCell();
			let date = new Date();
			dateCell.innerHTML = date.toDateString();
		});
}