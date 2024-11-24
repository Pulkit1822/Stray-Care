import { Loader } from '@googlemaps/js-api-loader';

const GOOGLE_MAPS_API_KEY = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;

const loader = new Loader({
  apiKey: GOOGLE_MAPS_API_KEY,
  version: 'weekly',
  libraries: ['places'],
});

export const initMap = async (elementId, options = {}) => {
  try {
    await loader.load();
    const element = document.getElementById(elementId);
    const map = new google.maps.Map(element, {
      center: { lat: 20.5937, lng: 78.9629 }, // India center
      zoom: 5,
      ...options,
    });
    return map;
  } catch (error) {
    console.error('Error loading Google Maps:', error);
    throw error;
  }
};

export const addMarker = (map, position, options = {}) => {
  return new google.maps.Marker({
    map,
    position,
    ...options,
  });
};
