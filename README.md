![image](https://github.com/user-attachments/assets/56a5b62f-3814-4db1-80cb-0a9f20f9e637)

# YellowDotDecode

**YellowDotDecode** is a graphical application that decodes the hidden information embedded in the yellow dots printed by some printers. These yellow dots, often invisible to the naked eye, contain metadata such as the date, time, and serial number of the printer, which can be used to trace the source of a printed document.

The application is based on the decoding method described in the [Chaos Computer Club (CCC) research paper](https://www.eff.org/files/filenode/printers/ccc.pdf).

## Features

- Simple graphical interface for inputting the yellow dot matrix manually.
- Automatic decoding of information such as date, time, and printer serial number.
- Displays decoded results in a user-friendly format.
- Ability to save decoded data for future analysis.

## Prerequisites

Before using DotDecode, make sure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `tkinter` (for the graphical interface)

You can install these dependencies using the following command:

```bash
pip install tk
```

## Installation

1. Clone the DotDecode repository:

   ```bash
   git clone https://github.com/Natounet/YellowDotDecode.git
   ```

2. Navigate to the project directory:

   ```bash
   cd YellowDotDecode
   ```

3. Run the application:

   ```bash
   python decode.py
   ```

## Usage

### Step 1: Prepare the yellow dots
1. Scan the printed document containing the yellow dots.
2. Make sure the scan is high quality and the yellow dots are clearly visible.
3. Identify the yellow dot matrix either manually or using third-party software.

![Yellow dots exemple](https://i.imgur.com/08zHlUk.png)

*Source: Chaos Computer Club (CCC)*

### Step 2: Input the yellow dots matrix
1. Open **YellowDotDecode**.
2. On the graphical grid, manually check the boxes corresponding to the yellow dots present in your scanned document, as shown in the image below:

![Yellow Dot exemple detailed](https://i.imgur.com/ul87NOZ.png)

*Source: Chaos Computer Club (CCC)*

![YellowDotDecode GUI](https://i.imgur.com/zDogM2h.png)

   Each checkbox represents a potential yellow dot. Click to mark the ones that are visible in the scanned document.

### Step 3: Decode the information
1. Once you have entered the yellow dot matrix, click the **"Decode Pattern"** button.
2. The decoded information (such as date, time, and printer serial number) will be displayed in the lower text box.

   Example decoded output:

   ```
   HH:MM  DD/MM/YY  SN
   12:50  21/06/05  21052857
   ```

### Step 4: Save the results (optional)
You can copy the decoded information for further analysis or save it manually to a file.

## License

This project is licensed under the MIT License.
