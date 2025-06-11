<<<<<<< HEAD
# Vesti 🌱


## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [File Descriptions](#file-descriptions)
4. [Presentation Source Links](#presentation-source-links)


## Introduction

Vesti is an app for iOS devices that helps customers shop more sustainably. Often when we shop, it’s difficult to determine whether we’re making sustainable choices with the products we buy without extensive research beforehand. That’s where Vesti comes in. Users can take a photo of the product they are considering buying, upload images of a product’s barcode, and Vesti will provide a “green rating” (GR) out of 10 for both the product itself (based on its component materials) and the brand (based on their sustainability initiatives). If users wish, they may also click a button to view Vesti’s reasoning for the sustainability scores, allowing them to make more informed choices to shop in a more eco-friendly manner.


## Features

- Barcode image upload: Users can upload an image of the barcode on the tag of the product they wish to purchase.
- Green rating: Vesti provides a sustainability score for both the product and the brand.
- Product/brand info: Vesti provides a more detailed summary of its reasonings


## File Descriptions

**allergen_info.py:**  It is in charge of giving the user a short description of the products that are being used in the product and, with that, it also identifies allergens and associated hazards the product has. Finally, all this data is printed. 

**brand_info.py:**  This code is designed to evaluate the product for sustainability and humanitarianism. After identifying these variables, alternative brands are suggested at a similar price point.  

**image_analysis.py:**  Processes the image that the user inputs, extracts the numbers from the barcode image and returns them in JSON format. 

**product_database.py:** Contains database of sample store inventory. Database contains products (e.g. shirts, pants, sunglasses, etc.) as individual entries, with each entry containing the brand name, product type, and list of component materials. Each entry also corresponds to a key, which is the product’s barcode number. Also contains functionality to search for specific barcode numbers based on the image the user uploads and returns all information stored in each entry.

**main.py:** The code is in charge of taking the barcode image, match it with a number in the database to identify which product they are talking about, retrieves all the details and information that were previously identified (allergens, sustainability, information about the product, etc) and shows it all to the user.

**product_info.py:** The code is in charge of getting information about a product, like the sustainability rating and description, based on a product's details.


## Presentation Source Links
1. https://pmc.ncbi.nlm.nih.gov/articles/PMC8257395/
2. https://www.statista.com/statistics/1305696/apparel-industry-co2e-emissions/
3. https://www.uniformmarket.com/statistics/fast-fashion-statistics
=======
# Welcome to your Expo app 👋

This is an [Expo](https://expo.dev) project created with [`create-expo-app`](https://www.npmjs.com/package/create-expo-app).

## Get started

1. Install dependencies

   ```bash
   npm install
   ```

2. Start the app

   ```bash
   npx expo start
   ```

In the output, you'll find options to open the app in a

- [development build](https://docs.expo.dev/develop/development-builds/introduction/)
- [Android emulator](https://docs.expo.dev/workflow/android-studio-emulator/)
- [iOS simulator](https://docs.expo.dev/workflow/ios-simulator/)
- [Expo Go](https://expo.dev/go), a limited sandbox for trying out app development with Expo

You can start developing by editing the files inside the **app** directory. This project uses [file-based routing](https://docs.expo.dev/router/introduction).

## Get a fresh project

When you're ready, run:

```bash
npm run reset-project
```

This command will move the starter code to the **app-example** directory and create a blank **app** directory where you can start developing.

## Learn more

To learn more about developing your project with Expo, look at the following resources:

- [Expo documentation](https://docs.expo.dev/): Learn fundamentals, or go into advanced topics with our [guides](https://docs.expo.dev/guides).
- [Learn Expo tutorial](https://docs.expo.dev/tutorial/introduction/): Follow a step-by-step tutorial where you'll create a project that runs on Android, iOS, and the web.

## Join the community

Join our community of developers creating universal apps.

- [Expo on GitHub](https://github.com/expo/expo): View our open source platform and contribute.
- [Discord community](https://chat.expo.dev): Chat with Expo users and ask questions.
>>>>>>> 11806a6 (Initial commit)
