// no particular background tasks
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.action === "openPrompt") {
    chrome.runtime.openOptionsPage();
  }
});

// Function to send message to content script
function sendMessageToContentScript(message) {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.sendMessage(tabs[0].id, message);
  });
}
