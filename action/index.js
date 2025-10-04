const core = require('@actions/core');

try {
  // Get input from workflow
  const message = core.getInput('message');
  
  console.log(message);

  // Set an output
  core.setOutput('outputMessage', message + ' ✅');
} catch (error) {
  core.setFailed(error.message);
}
