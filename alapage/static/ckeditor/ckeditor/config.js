/**
 * Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	config.allowedContent = true;
	config.startupFocus = true;
};

CKEDITOR.on('instanceReady',
   function( evt ) {
      var instanceName = 'id_content'; // the HTML id configured for editor
      var editor = CKEDITOR.instances[instanceName]; 
      editor.execCommand('maximize');
   }
 );