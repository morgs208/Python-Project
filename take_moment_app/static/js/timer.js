// Found this code from a video as I searched the internet for many different examples and this one made the most sense to me.


var active = false;

function start_timer() {
    if (active) {
        var timer = document.getElementById("my_timer").innerHTML;
        var arr = timer.split(":");
        var hour = arr[0];
        var min = arr[1];
        var sec = arr[2];

        if (sec == 59) {
            if (min == 59) {
                hour ++;
                min = 0;
                if (hour < 10) hour = "0" + hour;
            }   else {
                min ++;
            }
           if (min < 10) min = "0" + min;
            sec = 0;
        }   else {
            sec ++;
            if (sec < 10) sec ="0" + sec;
        }

        document.getElementById("my_timer").innerHTML = hour + ":" + min + ":" + sec;
        setTimeout(start_timer, 1000);
    }
}

function change() {
    if (active == false) {
        active = true;
        start_timer();
        document.getElementById("control").innerHTML = "Stop";
    } else {
        active = false;
        document.getElementById("control").innerHTML = "Start";
    }
}

function reset() {
    document.getElementById("my_timer").innerHTML = "00" + ":" + "00" + ":" + "00";
}
