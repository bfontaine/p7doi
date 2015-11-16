(function() {
  var form  = document.getElementById('doi-form'),
      input = document.getElementById('doi-text'),

      BASEURL = 'http://rproxy.sc.univ-paris-diderot.fr/login' +
        '?url=http://dx.doi.org/';

  function openDOI(doi) {
    document.location = BASEURL + doi.replace(/^\s+|\s+$/g, '');
  }

  form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    openDOI(input.value);
  }, false);

  var anchor = document.location.hash.slice(1);
  if (anchor !== "") {
    openDOI(anchor);
  }

})();
