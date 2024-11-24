import axios from 'axios';

const API_BASE_URL= import.meta.env.VITE_API_BASE_URL;


const api= axios.create({

  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config)=> {
  const token= localStorage.getItem('token');
  if (token) {
    config.headers.Authorization= `Bearer ${token}`;
  }
  return config;
});

export const alertsApi= {
  getAlerts: ()=> api.get('/alerts'),
  getAlert: (id)=> api.get(`/alerts/${id}`),
  createAlert: (data)=> api.post('/alerts', data),
  updateAlert: (id, data)=> api.put(`/alerts/${id}`, data),
};


export const detectionApi= {
  analyzeImage: (image)=> {
    const formData= new FormData();
    formData.append('image', image);
    return api.post('/detection/analyze', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
  },
  processStream: (data)=> api.post('/detection/stream', data),
};

export const analyticsApi= {
  getStats: ()=> api.get('/analytics/stats'),
  getHistory: (params)=> api.get('/analytics/history', { params }),
};
