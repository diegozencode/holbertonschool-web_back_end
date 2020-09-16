export default function handleResponseFromAPI(promise) {
  promise.resolve().then(() => {
    console.log('Got a response from the API');
    return {
      status: 200,
      body: 'success',
    };
  });
  promise.reject().then(() => {
    console.log('Got a response from the API');
    return Error();
  })
    .catch(Error);
}
