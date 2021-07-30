var Twitter = requiere('twitter');

const cliente = new Twitter({
    consume_key:"ulIyy3tdHD2ICYAQuLfmaPFY3",
    consumer_secret:"pF63JdlSd8mYIsWLP4KVnoZG8DIRRP9HsEv2nfMZ1FVHKQZVdJ",
    access_token: "1419713857514311681-pIrCxJOHrWk2mOXtYTjL4zzuRSnxbS",
    access_token_secret: "y3gueu71x60uIvnHOxZc6okYWpBmijoiTHFOwUgBUPjx9"
})

cliente.post("statuses/update", {status: "pruebaa"})
    .then((tweet) => {
        console.log(tweet);
    })
    .catch((err) => {
        console.log(error);
    })