<?php
    //Use in the "Post-Receive URL's" section of your GitHub Repo
if ( $_POST['payload'] ) {
    shell_exec('cd ~/singlepage && git pull');
}