Frontend: Adding a New Node
1. Create the Node Component
File: frontend/src/nodes/nodeX.js (replace X with your node number or name)

Create a new file for your node.

Import the shared BaseNode component.

Define and export your node component, passing props to BaseNode.

2. Declare Node Fields in nodeConfigs.js
File: nodeConfigs.js

Add a new entry for your node in the exported config object.

Specify:

label: Display name for the node.

fields: An array of field definitions (type, name, label, options, etc.).

inputs/outputs: Handle definitions for connections.

(Optional) style: Custom styles or colors for the node.

3. Import the Node in ui.js
File: ui.js

Import your new node component at the top of the file.

Add it to the nodeTypes object, mapping the config key to the component.

4. Update the Toolbar or Node Palette
File: (Wherever your toolbar/palette is defined, e.g., frontend/src/components/Toolbar.js)

Add a button or a draggable item for your new node.

Ensure it uses the correct type/key as defined in nodeConfigs.js.

5. Test the Node in the App
Start your frontend app.

Add your new node from the toolbar/palette to the canvas.

Check that:

The node renders correctly.

Fields appear and are editable.

Handles allow connections.

Data flows as expected.

6. (Optional) Add Node-Specific Logic
If your node needs custom behavior, add it in the component or extend the abstraction as needed.

Backend: FastAPI Workflow Overview
1. Receive Pipeline Data
Endpoint: /pipelines/parse

Receives: JSON with nodes and edges arrays from the frontend.

2. Parse and Validate Pipeline
Steps:

Count nodes and edges.

Check if the pipeline graph is a Directed Acyclic Graph (DAG) using the provided utility.

3. Respond to Frontend
Returns: JSON with node/edge counts and DAG status.

4. (Optional) Extend Backend Logic
Add endpoints for:

Executing pipelines.

Validating node data.

Saving/loading pipelines.

Integrating with databases or external APIs.

Summary Table
Step	File(s)	Action
1	src/nodes/nodeX.js	Create node component using BaseNode
2	src/nodes/nodeConfigs.js	Add node config: label, fields, handles, style
3	src/ui.js	Import node, add to nodeTypes
4	Toolbar/Palette	Add node to UI for user access
5	App	Test node rendering and connections
6 (Optional)		Add custom logic if needed
Backend	main.py	Receives
