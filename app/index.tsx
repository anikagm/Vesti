import React from 'react';
import { Image, StyleSheet, View } from 'react-native';
import vestiLogo from '../assets/images/vesti-logo.png';

const VestiCircleLogo = () => {
  return (
    <View style={styles.container}>
      <View style={styles.circleWrapper}>
        <View style={styles.circle} />
        <View style={[styles.circle, styles.overlappingCircle]} />
        <Image source={vestiLogo} style={styles.image} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center',
    backgroundColor: '#fff',
    paddingBottom: 100,
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
});

export default VestiCircleLogo;

