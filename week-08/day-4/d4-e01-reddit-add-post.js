'use strict';

window.onload = function() {

  function sendPostEequest() {
    const redditReq = new XMLHttpRequest();

    httpRequest.open('POST', 'http://secure-reddit.herokuapp.com/simple/posts');
    httpRequest.setRequestHeader('Accept', 'application/json');
    httpRequest.setRequestHeader('Content-type', 'application/json');
    httpRequest.send(JSON.stringify(post));

    redditReq.onreadystatechange = function() {
      if (redditReq.readyState === XMLHttpRequest.DONE && redditReq.status === 200) {
        console.log('HTTP REQUEST SUCCESSFUL');
      }
    };
    redditReq.onload = function() {
      if (redditReq.status >= 200 && redditReq.status < 400) {
        console.log('Posting succesful, loading index.html page...');
        window.location = 'index.html';
      } else {
        console.log('Reached the API, but it returned an error');
      }
    }
  }
  
  document.querySelector('form').addEventListener('submit', sendPostEequest);


  let post = {
    title: ' + postTitle.value + ',
    url: ' + postUrl.value + ',
  };

  
};