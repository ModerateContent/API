![alt text](https://www.moderatecontent.com/img/logo.png "ModerateContent.com")

### ModerateContent.com - The FREE Content Moderation API (https://www.moderatecontent.com)

Our free API provides a content rating for any image. Detect inappropriate content from adult to violent and more subtle ratings including smoking, alcohol and suggestive.

Example's of how to use the API
* [Javascript - jQuery && AJAX && GET](../blob/master/Example-JS-JQUERY_AJAX_GET/)
* [Javascript - jQuery && AJAX && POST](../blob/master/Example-JS-JQUERY_AJAX_POST/)
* [Javascript - jQuery && AJAX && JSONP && POST](../blob/master/Example-JS-JQUERY_AJAX_JSONP_GET/)
* [Javascript - AJAX && GET](../blob/master/Example-JS-AJAX_GET/)
* [Javascript - AJAX && POST](../blob/master/Example-JS-AJAX_POST/)
* [Javascript - AJAX && JSONP && POST](../blob/master/Example-JS-AJAX_JSONP_GET/)
* [PHP - CURL && GET](../blob/master/Example-PHP-CURL_GET/)
* [PHP - file_get_contents](../blob/master/Example-PHP-FILE_GET_CONTENTS/)
* [CURL - GET](../blob/master/Example-CURL/)

```javascript
$.ajax('https://www.moderatecontent.com/api/', {
    method: "GET",
    dataType: 'json',
    data: {url: 'http://www.moderatecontent.com/img/logo.png'},
    success: function (response) {
        console.log(response);
    }
});

```