// Auto-dismiss alerts after 4 seconds
document.addEventListener('DOMContentLoaded', function(){
	setTimeout(function(){
		document.querySelectorAll('.alert').forEach(function(a){
			a.classList.add('fade');
			a.classList.remove('show');
			try{ a.remove(); }catch(e){}
		});
	}, 4000);

	// Image preview for problem post
	var fileInput = document.querySelector('input[type=file][name="image"]');
	var preview = document.getElementById('preview');
	if(fileInput && preview){
		fileInput.addEventListener('change', function(e){
			var file = e.target.files[0];
			if(!file) { preview.style.display='none'; preview.src=''; return; }
			var reader = new FileReader();
			reader.onload = function(ev){
				preview.src = ev.target.result;
				preview.style.display = 'block';
			};
			reader.readAsDataURL(file);
		});
	}
});

