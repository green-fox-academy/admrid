'use strict';

window.onload = function() {

  let redditReq = new XMLHttpRequest();
  let redditPosts;

  redditReq.open("GET", "https://time-radish.glitch.me/posts");
  redditReq.send();

  let building = function(toProcess) {
    // let redditPostsList = document.createElement('ul');
    // document.body.appendChild(redditPostsList);
    toProcess.forEach(post => { 
      let mainDiv = document.querySelector('main');
      let redditPost = document.createElement('section');
      let redditPostVote = document.createElement('section');
      let redditPostVoteUp = document.createElement('button');
      let redditPostVoteCount = document.createElement('p');
      let redditPostVoteDown = document.createElement('button');
      let redditPostContent = document.createElement('section');
      let redditPostHeader = document.createElement('h2');
      let redditPostDate = document.createElement('p');
      let redditPostModify = document.createElement('a');
      let redditPostRemove = document.createElement('a');
      
      redditPostVoteCount.innerText = post.score;
      redditPostHeader.innerHTML = `<a href="${post.url}">${post.title}</a>`;
      redditPostDate.innerHTML = `submitted ${post.timestamp} ago by <a href="">${post.owner}</a>`;
      redditPostModify.innerHTML = `<a href="">modify</a>`;
      redditPostRemove.innerHTML = `<a href="">remove</a>`;

      mainDiv.classList.add('main');
      redditPost.classList.add('post');
      redditPostVote.classList.add('vote');
      redditPostVoteUp.classList.add('upvote');
      redditPostVoteDown.classList.add('downvote');
      redditPostVoteCount.classList.add('voteCount');
      redditPostContent.classList.add('post-content');

      mainDiv.appendChild(redditPost);
      redditPost.appendChild(redditPostVote);
      redditPost.appendChild(redditPostContent);
      redditPostVote.appendChild(redditPostVoteUp);
      redditPostVote.appendChild(redditPostVoteCount);
      redditPostVote.appendChild(redditPostVoteDown);
      redditPostContent.appendChild(redditPostHeader);
      redditPostContent.appendChild(redditPostDate);
      redditPostContent.appendChild(redditPostModify);
      redditPostContent.appendChild(redditPostRemove);
    });
  };

  redditReq.onreadystatechange = function() {
    if (redditReq.readyState === XMLHttpRequest.DONE && redditReq.status === 200) {
      redditPosts = JSON.parse(redditReq.response);
      // console.log(redditReq);
      console.log('posts.response: ', redditPosts.response);
      console.log('posts: ', redditPosts);
      console.log('posts posts: ', redditPosts.posts);
      building(redditPosts.posts);
    }
  };
};
