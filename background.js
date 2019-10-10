/**
Name: xssAuto
Author: z0id
Bug Bounty Tool
**/
browser.browserAction.onClicked.addListener(run);

// Run the program.
function run() {
	readTextFile();
}

// Read the text file.
function readTextFile()
{
	const logFileText = async file => {
		  var index = 0;
    	response = await fetch(file)
    	text = await response.text()
    	url = text.split("\n");
    	console.log(url[index]);
    	setInterval(() => {
    		if (index <= url.length - 1) {
				  loadURL(url[index]);
          index = index + 1;
        }
		}, 5000);
 
    }
    logFileText("hosts.txt");
}


// Load the links
function loadURL(link) {

	browser.notifications.create({
  		"type": "basic",
  		"iconUrl": "src48x48.png",
  		"title": "Notification",
 	 	"message": link
	});

	// Update the tab
  	var creating = browser.tabs.update({
    	url:link
  	});
}