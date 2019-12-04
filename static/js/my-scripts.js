// (function nextMovie() {
//    var img1 = "http://placehold.it/350x150";
//    var img2 = "http://placehold.it/200x200";
//
//    var imgElement = document.getElementById('toggleImage');
//
//    imgElement.src = (imgElement.src === img1)? img2 : img1;
// });

// function nextMovie() {
//     var src = "http://google.com/images/logo.gif";
//     show_image("http://google.com/images/logo.gif", 276,110, "Google Logo");
// }
//
// function show_image(src, width, height, alt) {
//     var img = document.createElement("img");
//     img.src = src;
//     img.width = width;
//     img.height = height;
//     img.alt = alt;
//     document.body.appendChild(img);
// }

// function showNextMovie(src) {
//     var img = document.createElement("img");
//     img.src = src;
//     document.body.appendChild(img);
// };
var counter = 0;
user_ratings = []
url_list = ['https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://m.media-amazon.com/images/M/MV5BMTYwNjAyODIyMF5BMl5BanBnXkFtZTYwNDMwMDk2._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://m.media-amazon.com/images/M/MV5BMTQzMjYwNTc2M15BMl5BanBnXkFtZTcwMTY0Mjc4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://m.media-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://m.media-amazon.com/images/M/MV5BMjE4MDYzNDE1OV5BMl5BanBnXkFtZTcwNDY2OTYwNA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://m.media-amazon.com/images/M/MV5BMTYzZWE3MDAtZjZkMi00MzhlLTlhZDUtNmI2Zjg3OWVlZWI0XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg'];

function showNextMovie(rating) {
    var img = document.getElementById("currentImage");
    img.src = url_list[counter];
    user_ratings.push(rating)
    increaseCounter()
};


// Function to increment counter
function increaseCounter() {
    if (counter == url_list.length) {
        counter = 0;
    }
    else {
        counter += 1;
    }
};

document.getElementById("bad").addEventListener("click", showNextMovie(1));
document.getElementById("unknown").addEventListener("click", showNextMovie(0));
document.getElementById("good").addEventListener("click", showNextMovie(5));


// function badMovie(){
//     user_ratings.push(1)
//     showNextMovie()
//     increaseCounter()
// };
//
// function unknownMovie(){
//     user_ratings.push(0)
//     showNextMovie()
//     increaseCounter()
// };
//
// function goodMovie(5){
//     user_ratings.push(1)
//     showNextMovie()
//     increaseCounter()
// };
