$(document).ready(function() {
	var pathname = window.location.pathname;

	// BOARD
	$("a[link='" + pathname + "']").parent().attr("class", "active");

	var tags = [
		"Безопасность - не предел!",
		"Не всякий может смотреть в будущее",
		"Мы лучше всех знаем, что Вам нужно!",
		"Мы не следим, мы интересуемся",
		"Мы опаснее преступников",
		"Сила, дисциплина, стиль",
		"Мы знаем, что Вы делали прошлым летом...",
		"365/12/24/7"
	];
	var tag = tags[Math.floor(Math.random() * tags.length)];
	$("#navBarText").text(tag);

	// Redirect Buttons
	$(".redirectButton").click(function (element) {
		// var link = element.currentTarget.attributes.link.nodeValue;
		var link = $(this).attr("link");
		if (pathname === link) { }
		else {
			$("#content").LoadingOverlay("show", {
			image: "/static/img/loading.gif"
			});
			document.location.pathname = link;
		}
	});

	$(".lecturer-preview-link").click(function() {
			var id = $(this).attr("lecturer-id");
			// console.log(id);
			// var id = 2;
			$("#myModal").load("/board/lecturer_modal/"+id);
			// $("#myModal").text(id);			
	});
});	