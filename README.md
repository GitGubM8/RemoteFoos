# Installation
1. Python 3.6
2. `pip install slackclient==2.5.0`

# Style
Coming from a C# background, this project rarely follows PEP8 format

- Collapse all blocks when reading
  - Only open up blocks when implementation details are needed
  - Closely related classes/fields/properties/methods do not have a blank line next to each other

- Import order follows Architecture hierachy
  - More important dependencies are imported first

- Non-static classes follow IReadWrite templates
  - Provides better co/contravariance support
  - Allows better restrictions and permissions control

- Tabs
  - It's a character designed for indentation
  - You can probably visually tune how much spacing you want out of each tab in your IDE
