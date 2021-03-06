var token = "";
var tuid = "";

var twitch = window.Twitch.ext;

function setAuth(token) {
  Object.keys(requests).forEach((req) => {
      twitch.rig.log('Setting auth headers');
      requests[req].headers = { 'Authorization': 'Bearer ' + token }
  });
}

twitch.onContext(function(context) {
  twitch.rig.log(context);
});

twitch.onAuthorized(function(auth) {
  // save our credentials
  token = auth.token;
  tuid = auth.userId;

  // enable the button
  $('#cycle').removeAttr('disabled');

  setAuth(token);
});

function updateBlock(hex) {
    $('#color').css('background-color', hex);
}

function getRandomColor() {
  return '#'+Math.floor(Math.random()*16777215).toString(16);
}

$(function() {
    $('#cycle').prop('disabled', false);

    $('#cycle').click(function() {
      updateBlock(getRandomColor());
    });
    
    const fetchCoordinates = () => {
		      window.setTimeout(async () => {
		      	const res = await fetch("https://pawn.boardengineer.net/read");

		        const data = await res.text();
		        console.log('data', data);
		        const [x, y] = data.split(',');

		        

                $('#piece').css('top', Number.parseInt(y, 10) * 20);
                $('#piece').css('left', Number.parseInt(x, 10) * 20);
		        

		        // continue fetching every 1000ms
		        fetchCoordinates();
		      }, 1000);
		    };

			fetchCoordinates()
});
