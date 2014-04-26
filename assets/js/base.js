/ Editors manager ``miu`` methods

// Initialize editor using default settings extended with ``extraSettings``
miu.init(textareaId, extraSettings);

// Get default mIu settings
miu.settings();

// Set default mIu settings
miu.settings(newSettings);

// Get all initialized aditors
miu.editors();

// Get certain editor
miu.editors(textareaId);


// Editor instance methods

// Dynamically add button at ``index`` position
editor.addButton(conf, index)

// Dynamically remove button at ``index`` position
editor.removeButton(index)
