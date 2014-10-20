(function() {
  var form  = document.getElementById('doi-form'),
      input = document.getElementById('doi-text'),

      BASEURL = 'http://rproxy.sc.univ-paris-diderot.fr/login' +
        '?url=http://dx.doi.org/';

  form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    var doi = input.value.replace(/^\s+|\s+$/g, ''),
        url = BASEURL + doi;

    document.location = url;

  }, false);

})();
