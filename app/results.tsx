import React, { useState } from 'react';
import { Pressable, SafeAreaView, StyleSheet, Text } from 'react-native';


const VestiResultsPage = () => {
  const [showText, setShowText] = useState(false);

   return (
    <SafeAreaView style={styles.container}>

      <SafeAreaView style={styles.buttonShadow} />

      <Pressable style={styles.button} onPress={() => setShowText(!showText)}>
        <Text style={{fontFamily: 'Verdana', fontSize: 17, color: '#8A4700'}}>Click to explore sustainability info:</Text>    
      </Pressable>
      {showText &&
        <SafeAreaView style={styles.textContainer}>
        <SafeAreaView style={styles.productInfoContainer}> 
          <Text style={styles.titleText}> product sustainability info {'\n'} </Text>
          <Text style={styles.normalText}>
            The product features a mix of natural and synthetic materials, with cotton and lyocell providing an eco-friendly base, but synthetic components somewhat reducing overall sustainability.
          </Text> 
        </SafeAreaView> 
        
        <SafeAreaView style={styles.brandInfoContainer}> 
          <Text style={styles.titleText}> brand sustainability info {'\n'}  </Text>
          <Text style={styles.normalText}>
            Levi's prioritizes sustainability with responsible supply chains, water conservation, and recycling, reducing environmental impact while addressing social and labor concerns with ongoing efforts gradually.
          </Text> 
        </SafeAreaView>
        </SafeAreaView>}

    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center',
    backgroundColor: '#C6D8AA',
    paddingBottom: 100,
    borderWidth: 17,
    borderColor: '#8FBE7B',
    borderRadius: 30
  },
  circleWrapper: {
    width: 200,
    height: 200,
    position: 'relative',
    marginLeft: 22,
  },
  circle: {
    width: 180,
    height: 180,
    borderRadius: 90,
    backgroundColor: '#F4BADC',
    position: 'absolute',
    top: 0,
    left: 0,
  },
  overlappingCircle: {
    top: -6,
    left: -6,
    backgroundColor: '#F7D2E8',
  },
  image: {
    position: 'absolute',
    top: 21,
    left: 20,
    width: 132,
    height: 132,
    resizeMode: 'contain',
  },
  button: {
    marginBottom: 20,
    paddingVertical: 10,
    paddingHorizontal: 20,
    backgroundColor: '#F7D2E8'
  },
  buttonShadow: {
    width: 335,
    height: 40,
    backgroundColor: '#F4BADC',
    position: 'relative',
    top: 47,
    left: 7
  },
  textContainer: {
    width: 300,
    height: 100,
    justifyContent: 'space-evenly',
    flexDirection: 'row'

  },
  productInfoContainer: {
    width: 170,
    height: 100,
    marginRight: 10,
    justifyContent: 'center',
    alignItems: 'center'
  },
  brandInfoContainer: {
    width: 170,
    height: 100,
    justifyContent: 'center',
    alignItems: 'center',
  },
  titleText: {
    fontWeight: 'bold',
    fontFamily: 'Verdana', 
    fontSize: 9, 
    color: '#8A4700', 
    textAlign: 'center',
  },
  normalText: {
    fontFamily: 'Verdana', 
    fontSize: 9, 
    color: '#8A4700', 
    textAlign: 'center', 
    marginLeft: 6,
    marginRight: 6,
    marginBottom: 6,
    marginTop: 3
  }
});

export default VestiResultsPage;

