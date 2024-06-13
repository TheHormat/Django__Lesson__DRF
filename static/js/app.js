const cards = document.querySelector(".cards");

fetch("http://127.0.0.1:8000/blog-api/list/")
  .then((res) => res.json())
  .then((data) => data.map((blog) => createCard(blog)));

function createCard(blog) {
  const cardDiv = `
  <div class="col-lg-4 col-md-6 col-sm-12 mb-4">
    <div class="card" style="width: 100%;">
      <img src="${blog.image}" class="card-img-top">
        <div class="card-body">
            <h5 class="card-title">${blog.title}</h5>
            <p class="card-text">${blog.content}</p>
            <a href="#" class="btn btn-primary">Detail</a>
        </div>
    </div>
  </div>`;
  cards.innerHTML += cardDiv;
}
