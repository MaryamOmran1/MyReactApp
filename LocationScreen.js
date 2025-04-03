import React from 'react';
import { View, Text } from 'react-native';
import * as Location from 'expo-location';

export const LocationScreen = () => {
  const getLocation = async () => {
    let { status } = await Location.requestForegroundPermissionsAsync();
    if (status === 'granted') {
      let location = await Location.getCurrentPositionAsync({});
      console.log(location);
    }
  };

  React.useEffect(() => {
    getLocation();
  }, []);

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Location Screen</Text>
    </View>
  );
};