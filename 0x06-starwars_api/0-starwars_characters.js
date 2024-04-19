#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const charactersUrls = JSON.parse(body).characters;
    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        }
      });
    });
  }
});
