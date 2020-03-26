function onPageLoad(){
    console.log( "document loaded" );
    var url1 = "http://127.0.0.1:5000/get_home_teams"; 
    $.get(url1,function(data, status) {
        console.log("got response for get_home_teams request");
        if(data) {
            var home_team = data.home_team;
            var uihome = document.getElementById("uihome");
            $('#uihome').empty();
            for(var i in home_team) {
                var opt = new Option(home_team[i]);
                $('#uihome').append(opt);
            }
        }
    });

    var url2 = "http://127.0.0.1:5000/get_away_teams"; 
    $.get(url2,function(data, status) {
        console.log("got response for get_home_teams request");
        if(data) {
            var away_team = data.away_team;
            var uiaway = document.getElementById("uiaway");
            $('#uiaway').empty();
            for(var i in away_team) {
                var opt = new Option(away_team[i]);
                $('#uiaway').append(opt);
            }
        }
    });
}

function onClickedPredictWinner() {
    console.log("Predict Winner button clicked");
    var home_team = document.getElementById("uihome");
    var away_team = document.getElementById("uiaway");
    
    var winner = document.getElementById("uiPredictWinner");
  
    var url = "http://127.0.0.1:5000/predict_winner"; 
    
    $.post(url, {
        home_team: home_team.value,
        away_team: away_team.value
        
    },function(data, status) {
        console.log(data.predict_winner);
        if(data.predict_winner == 0)
            res = "HOME TEAM"
        else if(data.predict_winner == 1)
            res = "DRAW"
        else
            res = "AWAY TEAM"
        winner.innerHTML = "<h2>" + res + "</h2>";
        console.log(status);
    });
  }

window.onload = onPageLoad;