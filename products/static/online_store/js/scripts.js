window.document.getElementById("showButton").addEventListener("htmx:afterOnLoad", function() {
	setTimeout(function(){
		window.document.getElementById("modal").classList.add("uk-open")
	}, 10)
})


// This triggers the fade-out animation when the modal is closed.
window.document.getElementById("cancelButton").addEventListener("click", function() {
	window.document.getElementById("modal").classList.remove("uk-open")
	setTimeout(function(){
		window.document.getElementById("modals-here").innerHTML = ""
		,200
	})
})