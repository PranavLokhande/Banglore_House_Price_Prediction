{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "434a8e4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from matplotlib import pyplot as plt\n",
    "%matplotlib inline\n",
    "import matplotlib\n",
    "matplotlib.rcParams[\"figure.figsize\"]=(20,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ef528204",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>area_type</th>\n",
       "      <th>availability</th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>society</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>balcony</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Super built-up  Area</td>\n",
       "      <td>19-Dec</td>\n",
       "      <td>Electronic City Phase II</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>Coomee</td>\n",
       "      <td>1056</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>39.07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Plot  Area</td>\n",
       "      <td>Ready To Move</td>\n",
       "      <td>Chikka Tirupathi</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>Theanmp</td>\n",
       "      <td>2600</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>120.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Built-up  Area</td>\n",
       "      <td>Ready To Move</td>\n",
       "      <td>Uttarahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1440</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>62.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Super built-up  Area</td>\n",
       "      <td>Ready To Move</td>\n",
       "      <td>Lingadheeranahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>Soiewre</td>\n",
       "      <td>1521</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>95.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Super built-up  Area</td>\n",
       "      <td>Ready To Move</td>\n",
       "      <td>Kothanur</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1200</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>51.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              area_type   availability                  location       size  \\\n",
       "0  Super built-up  Area         19-Dec  Electronic City Phase II      2 BHK   \n",
       "1            Plot  Area  Ready To Move          Chikka Tirupathi  4 Bedroom   \n",
       "2        Built-up  Area  Ready To Move               Uttarahalli      3 BHK   \n",
       "3  Super built-up  Area  Ready To Move        Lingadheeranahalli      3 BHK   \n",
       "4  Super built-up  Area  Ready To Move                  Kothanur      2 BHK   \n",
       "\n",
       "   society total_sqft  bath  balcony   price  \n",
       "0  Coomee        1056   2.0      1.0   39.07  \n",
       "1  Theanmp       2600   5.0      3.0  120.00  \n",
       "2      NaN       1440   2.0      3.0   62.00  \n",
       "3  Soiewre       1521   3.0      1.0   95.00  \n",
       "4      NaN       1200   2.0      1.0   51.00  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1=pd.read_csv(\"bengaluru_house_prices.csv\")\n",
    "df1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e534e460",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(13320, 9)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a5fc4631",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method DataFrame.info of                   area_type   availability                  location  \\\n",
       "0      Super built-up  Area         19-Dec  Electronic City Phase II   \n",
       "1                Plot  Area  Ready To Move          Chikka Tirupathi   \n",
       "2            Built-up  Area  Ready To Move               Uttarahalli   \n",
       "3      Super built-up  Area  Ready To Move        Lingadheeranahalli   \n",
       "4      Super built-up  Area  Ready To Move                  Kothanur   \n",
       "...                     ...            ...                       ...   \n",
       "13315        Built-up  Area  Ready To Move                Whitefield   \n",
       "13316  Super built-up  Area  Ready To Move             Richards Town   \n",
       "13317        Built-up  Area  Ready To Move     Raja Rajeshwari Nagar   \n",
       "13318  Super built-up  Area         18-Jun           Padmanabhanagar   \n",
       "13319  Super built-up  Area  Ready To Move              Doddathoguru   \n",
       "\n",
       "            size  society total_sqft  bath  balcony   price  \n",
       "0          2 BHK  Coomee        1056   2.0      1.0   39.07  \n",
       "1      4 Bedroom  Theanmp       2600   5.0      3.0  120.00  \n",
       "2          3 BHK      NaN       1440   2.0      3.0   62.00  \n",
       "3          3 BHK  Soiewre       1521   3.0      1.0   95.00  \n",
       "4          2 BHK      NaN       1200   2.0      1.0   51.00  \n",
       "...          ...      ...        ...   ...      ...     ...  \n",
       "13315  5 Bedroom  ArsiaEx       3453   4.0      0.0  231.00  \n",
       "13316      4 BHK      NaN       3600   5.0      NaN  400.00  \n",
       "13317      2 BHK  Mahla T       1141   2.0      1.0   60.00  \n",
       "13318      4 BHK  SollyCl       4689   4.0      1.0  488.00  \n",
       "13319      1 BHK      NaN        550   1.0      1.0   17.00  \n",
       "\n",
       "[13320 rows x 9 columns]>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e4321381",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "area_type\n",
       "Built-up  Area          2418\n",
       "Carpet  Area              87\n",
       "Plot  Area              2025\n",
       "Super built-up  Area    8790\n",
       "Name: area_type, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.groupby('area_type')['area_type'].agg('count')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "cf385020",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Electronic City Phase II</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1056</td>\n",
       "      <td>2.0</td>\n",
       "      <td>39.07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Chikka Tirupathi</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>2600</td>\n",
       "      <td>5.0</td>\n",
       "      <td>120.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Uttarahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1440</td>\n",
       "      <td>2.0</td>\n",
       "      <td>62.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Lingadheeranahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1521</td>\n",
       "      <td>3.0</td>\n",
       "      <td>95.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kothanur</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1200</td>\n",
       "      <td>2.0</td>\n",
       "      <td>51.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   location       size total_sqft  bath   price\n",
       "0  Electronic City Phase II      2 BHK       1056   2.0   39.07\n",
       "1          Chikka Tirupathi  4 Bedroom       2600   5.0  120.00\n",
       "2               Uttarahalli      3 BHK       1440   2.0   62.00\n",
       "3        Lingadheeranahalli      3 BHK       1521   3.0   95.00\n",
       "4                  Kothanur      2 BHK       1200   2.0   51.00"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2=df1.drop(['area_type','society','balcony','availability'],axis=1) # not more use columnss....\n",
    "df2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "27427462",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "location       1\n",
       "size          16\n",
       "total_sqft     0\n",
       "bath          73\n",
       "price          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# data clesaning processs...\n",
    "df2.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1eb05f1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "location      0\n",
       "size          0\n",
       "total_sqft    0\n",
       "bath          0\n",
       "price         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=df2.dropna()\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "62664edf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Electronic City Phase II</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1056</td>\n",
       "      <td>2.0</td>\n",
       "      <td>39.07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Chikka Tirupathi</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>2600</td>\n",
       "      <td>5.0</td>\n",
       "      <td>120.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Uttarahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1440</td>\n",
       "      <td>2.0</td>\n",
       "      <td>62.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Lingadheeranahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1521</td>\n",
       "      <td>3.0</td>\n",
       "      <td>95.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kothanur</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1200</td>\n",
       "      <td>2.0</td>\n",
       "      <td>51.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   location       size total_sqft  bath   price\n",
       "0  Electronic City Phase II      2 BHK       1056   2.0   39.07\n",
       "1          Chikka Tirupathi  4 Bedroom       2600   5.0  120.00\n",
       "2               Uttarahalli      3 BHK       1440   2.0   62.00\n",
       "3        Lingadheeranahalli      3 BHK       1521   3.0   95.00\n",
       "4                  Kothanur      2 BHK       1200   2.0   51.00"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a98a7c9d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['2 BHK', '4 Bedroom', '3 BHK', '4 BHK', '6 Bedroom', '3 Bedroom',\n",
       "       '1 BHK', '1 RK', '1 Bedroom', '8 Bedroom', '2 Bedroom',\n",
       "       '7 Bedroom', '5 BHK', '7 BHK', '6 BHK', '5 Bedroom', '11 BHK',\n",
       "       '9 BHK', '9 Bedroom', '27 BHK', '10 Bedroom', '11 Bedroom',\n",
       "       '10 BHK', '19 BHK', '16 BHK', '43 Bedroom', '14 BHK', '8 BHK',\n",
       "       '12 Bedroom', '13 BHK', '18 Bedroom'], dtype=object)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['size'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e74dc9be",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HP\\AppData\\Local\\Temp\\ipykernel_11576\\3844813861.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df['bhk'] = df['size'].apply(lambda x: int(x.split(' ')[0]))\n"
     ]
    }
   ],
   "source": [
    "df['bhk'] = df['size'].apply(lambda x: int(x.split(' ')[0]))\n",
    "#Is code ka matlab yeh hai ki hum 'size' column me jo values hain unhe process karke 'bhk' column me store karna chahte hain. Iske liye humne ek lambda function use kiya hai jo har value ko split karta hai (space ke basis pe) aur pehla part (jo integer hai) usko convert karke 'bhk' column me daal deta hai.\n",
    "\n",
    "# Corrected code yeh hai:\n",
    "\n",
    "# python\n",
    "# Copy code\n",
    "# df['bhk'] = df['size'].apply(lambda x: int(x.split(' ')[0]))\n",
    "# df['size']: yeh dataframe ka 'size' column hai.\n",
    "# .apply(lambda x: ...): apply function use karte hain har value pe 'size' column me.\n",
    "# x.split(' '): yeh value ko space ke basis pe todta hai (split karta hai).\n",
    "# int(x.split(' ')[0]): split hone ke baad jo pehla part hai usko integer me convert karta hai.\n",
    "# Toh agar 'size' column me koi value '3 BHK' hai, toh yeh code usme se '3' ko nikaal ke integer me convert karke 'bhk' column me daal dega.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "af86dda6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Electronic City Phase II</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1056</td>\n",
       "      <td>2.0</td>\n",
       "      <td>39.07</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Chikka Tirupathi</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>2600</td>\n",
       "      <td>5.0</td>\n",
       "      <td>120.00</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Uttarahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1440</td>\n",
       "      <td>2.0</td>\n",
       "      <td>62.00</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Lingadheeranahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1521</td>\n",
       "      <td>3.0</td>\n",
       "      <td>95.00</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kothanur</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1200</td>\n",
       "      <td>2.0</td>\n",
       "      <td>51.00</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   location       size total_sqft  bath   price  bhk\n",
       "0  Electronic City Phase II      2 BHK       1056   2.0   39.07    2\n",
       "1          Chikka Tirupathi  4 Bedroom       2600   5.0  120.00    4\n",
       "2               Uttarahalli      3 BHK       1440   2.0   62.00    3\n",
       "3        Lingadheeranahalli      3 BHK       1521   3.0   95.00    3\n",
       "4                  Kothanur      2 BHK       1200   2.0   51.00    2"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "9895aed8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 2,  4,  3,  6,  1,  8,  7,  5, 11,  9, 27, 10, 19, 16, 43, 14, 12,\n",
       "       13, 18], dtype=int64)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['bhk'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "2a4b3fe9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1718</th>\n",
       "      <td>2Electronic City Phase II</td>\n",
       "      <td>27 BHK</td>\n",
       "      <td>8000</td>\n",
       "      <td>27.0</td>\n",
       "      <td>230.0</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4684</th>\n",
       "      <td>Munnekollal</td>\n",
       "      <td>43 Bedroom</td>\n",
       "      <td>2400</td>\n",
       "      <td>40.0</td>\n",
       "      <td>660.0</td>\n",
       "      <td>43</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       location        size total_sqft  bath  price  bhk\n",
       "1718  2Electronic City Phase II      27 BHK       8000  27.0  230.0   27\n",
       "4684                Munnekollal  43 Bedroom       2400  40.0  660.0   43"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.bhk>20]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "846eb54a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# we have erro ke bhai 2400 sq.ft main 43 bedroom kaise banenge toh error solve karna padenga apne koo..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "98ea19e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['1056', '2600', '1440', ..., '1133 - 1384', '774', '4689'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.total_sqft.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "cd709ffe",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_float(x):\n",
    "    try:\n",
    "        float(x)\n",
    "    except:\n",
    "        return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "b6c6080f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>Yelahanka</td>\n",
       "      <td>4 BHK</td>\n",
       "      <td>2100 - 2850</td>\n",
       "      <td>4.0</td>\n",
       "      <td>186.000</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122</th>\n",
       "      <td>Hebbal</td>\n",
       "      <td>4 BHK</td>\n",
       "      <td>3067 - 8156</td>\n",
       "      <td>4.0</td>\n",
       "      <td>477.000</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>137</th>\n",
       "      <td>8th Phase JP Nagar</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1042 - 1105</td>\n",
       "      <td>2.0</td>\n",
       "      <td>54.005</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>165</th>\n",
       "      <td>Sarjapur</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1145 - 1340</td>\n",
       "      <td>2.0</td>\n",
       "      <td>43.490</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>188</th>\n",
       "      <td>KR Puram</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1015 - 1540</td>\n",
       "      <td>2.0</td>\n",
       "      <td>56.800</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>410</th>\n",
       "      <td>Kengeri</td>\n",
       "      <td>1 BHK</td>\n",
       "      <td>34.46Sq. Meter</td>\n",
       "      <td>1.0</td>\n",
       "      <td>18.500</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>549</th>\n",
       "      <td>Hennur Road</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1195 - 1440</td>\n",
       "      <td>2.0</td>\n",
       "      <td>63.770</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>648</th>\n",
       "      <td>Arekere</td>\n",
       "      <td>9 Bedroom</td>\n",
       "      <td>4125Perch</td>\n",
       "      <td>9.0</td>\n",
       "      <td>265.000</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>661</th>\n",
       "      <td>Yelahanka</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1120 - 1145</td>\n",
       "      <td>2.0</td>\n",
       "      <td>48.130</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>672</th>\n",
       "      <td>Bettahalsoor</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>3090 - 5002</td>\n",
       "      <td>4.0</td>\n",
       "      <td>445.000</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               location       size      total_sqft  bath    price  bhk\n",
       "30            Yelahanka      4 BHK     2100 - 2850   4.0  186.000    4\n",
       "122              Hebbal      4 BHK     3067 - 8156   4.0  477.000    4\n",
       "137  8th Phase JP Nagar      2 BHK     1042 - 1105   2.0   54.005    2\n",
       "165            Sarjapur      2 BHK     1145 - 1340   2.0   43.490    2\n",
       "188            KR Puram      2 BHK     1015 - 1540   2.0   56.800    2\n",
       "410             Kengeri      1 BHK  34.46Sq. Meter   1.0   18.500    1\n",
       "549         Hennur Road      2 BHK     1195 - 1440   2.0   63.770    2\n",
       "648             Arekere  9 Bedroom       4125Perch   9.0  265.000    9\n",
       "661           Yelahanka      2 BHK     1120 - 1145   2.0   48.130    2\n",
       "672        Bettahalsoor  4 Bedroom     3090 - 5002   4.0  445.000    4"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[~df['total_sqft'].apply(is_float)].head(10)\n",
    "#It is an unstructured data contain non uniformity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "7ecdebca",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# baxically yejo 2100 - 2678 wala type ke no. ka average leke osko apan ne float me convert kara hainnn\n",
    "\n",
    "def convert_sqft_to_num(x):\n",
    "    tokens = x.split('-')\n",
    "    if len(tokens) == 2:\n",
    "        return (float(tokens[0]) + float(tokens[1])) / 2\n",
    "    try:\n",
    "        return float(x)\n",
    "    except:\n",
    "        return None\n",
    "\n",
    "#     def convert_sqft_to_num(x):: Yeh function define kar raha hai jo 'x' naam ka input lega.\n",
    "# tokens = x.split('-'): Yeh line input string 'x' ko '-' ke basis pe todta hai aur tokens naam ke list me store karta hai.\n",
    "# if len(tokens) == 2:: Agar tokens ki length 2 hai, matlab input 'x' me '-' tha.\n",
    "# return (float(tokens[0]) + float(tokens[1])) / 2: Agar '-' mila, toh tokens ko float me convert karke unka average return karta hai.\n",
    "# try:: Yeh block try karta hai input 'x' ko float me convert karne ka.\n",
    "# return float(x): Agar conversion successful hua, toh float value return karta hai.\n",
    "# except:: Agar conversion me koi error aaya, toh except block execute hoga.\n",
    "# return None: Error hone pe None return karta hai."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "7a21bcdd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "150.0"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "convert_sqft_to_num('100 - 200')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "c943ff9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100.0"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "convert_sqft_to_num('100')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "8d4f5c8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "convert_sqft_to_num('34.46Sq')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "5b255c18",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Electronic City Phase II</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1056.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>39.07</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Chikka Tirupathi</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>2600.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>120.00</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Uttarahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1440.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>62.00</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Lingadheeranahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1521.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>95.00</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kothanur</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1200.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>51.00</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   location       size  total_sqft  bath   price  bhk\n",
       "0  Electronic City Phase II      2 BHK      1056.0   2.0   39.07    2\n",
       "1          Chikka Tirupathi  4 Bedroom      2600.0   5.0  120.00    4\n",
       "2               Uttarahalli      3 BHK      1440.0   2.0   62.00    3\n",
       "3        Lingadheeranahalli      3 BHK      1521.0   3.0   95.00    3\n",
       "4                  Kothanur      2 BHK      1200.0   2.0   51.00    2"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3=df.copy()\n",
    "df3['total_sqft']=df3['total_sqft'].apply( convert_sqft_to_num)\n",
    "df3.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "2a23b6db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "location      Yelahanka\n",
       "size              4 BHK\n",
       "total_sqft       2475.0\n",
       "bath                4.0\n",
       "price             186.0\n",
       "bhk                   4\n",
       "Name: 30, dtype: object"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3.iloc[30]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "0158ed3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2475.0"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(2100+2850)/2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "0b18ce07",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Electronic City Phase II</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1056</td>\n",
       "      <td>2.0</td>\n",
       "      <td>39.07</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Chikka Tirupathi</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>2600</td>\n",
       "      <td>5.0</td>\n",
       "      <td>120.00</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Uttarahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1440</td>\n",
       "      <td>2.0</td>\n",
       "      <td>62.00</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Lingadheeranahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1521</td>\n",
       "      <td>3.0</td>\n",
       "      <td>95.00</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kothanur</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1200</td>\n",
       "      <td>2.0</td>\n",
       "      <td>51.00</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   location       size total_sqft  bath   price  bhk\n",
       "0  Electronic City Phase II      2 BHK       1056   2.0   39.07    2\n",
       "1          Chikka Tirupathi  4 Bedroom       2600   5.0  120.00    4\n",
       "2               Uttarahalli      3 BHK       1440   2.0   62.00    3\n",
       "3        Lingadheeranahalli      3 BHK       1521   3.0   95.00    3\n",
       "4                  Kothanur      2 BHK       1200   2.0   51.00    2"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1a182bb",
   "metadata": {},
   "source": [
    "# Feature Engineering --: adding columns to it pps"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "e185b4fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "      <th>price_per_sqft</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Electronic City Phase II</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1056.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>39.07</td>\n",
       "      <td>2</td>\n",
       "      <td>3699.810606</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Chikka Tirupathi</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>2600.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>120.00</td>\n",
       "      <td>4</td>\n",
       "      <td>4615.384615</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Uttarahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1440.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>62.00</td>\n",
       "      <td>3</td>\n",
       "      <td>4305.555556</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Lingadheeranahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1521.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>95.00</td>\n",
       "      <td>3</td>\n",
       "      <td>6245.890861</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kothanur</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1200.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>51.00</td>\n",
       "      <td>2</td>\n",
       "      <td>4250.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   location       size  total_sqft  bath   price  bhk  \\\n",
       "0  Electronic City Phase II      2 BHK      1056.0   2.0   39.07    2   \n",
       "1          Chikka Tirupathi  4 Bedroom      2600.0   5.0  120.00    4   \n",
       "2               Uttarahalli      3 BHK      1440.0   2.0   62.00    3   \n",
       "3        Lingadheeranahalli      3 BHK      1521.0   3.0   95.00    3   \n",
       "4                  Kothanur      2 BHK      1200.0   2.0   51.00    2   \n",
       "\n",
       "   price_per_sqft  \n",
       "0     3699.810606  \n",
       "1     4615.384615  \n",
       "2     4305.555556  \n",
       "3     6245.890861  \n",
       "4     4250.000000  "
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# df5=df3.copy()\n",
    "\n",
    "# feature engineering...\n",
    "\n",
    "# we createcolumns.....\n",
    "\n",
    "df5['price_per_sqft']=df5['price']*100000/df5['total_sqft']\n",
    "df5.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d84f966e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "245910ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1304"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(df5['location'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "4b4a2e55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "location\n",
       "Whitefield               535\n",
       "Sarjapur  Road           392\n",
       "Electronic City          304\n",
       "Kanakpura Road           266\n",
       "Thanisandra              236\n",
       "                        ... \n",
       "1 Giri Nagar               1\n",
       "Kanakapura Road,           1\n",
       "Kanakapura main  Road      1\n",
       "Karnataka Shabarimala      1\n",
       "whitefiled                 1\n",
       "Name: location, Length: 1293, dtype: int64"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df5.location=df5.location.apply(lambda x:x.strip())\n",
    "location_stats =df5.groupby('location')['location'].agg('count').sort_values(ascending=False)\n",
    "location_stats"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "71c309f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1052"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(location_stats[location_stats<=10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "9afd30ea",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "location\n",
       "Basapura                 10\n",
       "1st Block Koramangala    10\n",
       "Gunjur Palya             10\n",
       "Kalkere                  10\n",
       "Sector 1 HSR Layout      10\n",
       "                         ..\n",
       "1 Giri Nagar              1\n",
       "Kanakapura Road,          1\n",
       "Kanakapura main  Road     1\n",
       "Karnataka Shabarimala     1\n",
       "whitefiled                1\n",
       "Name: location, Length: 1052, dtype: int64"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "location_stats_less_than_10=location_stats[location_stats<=10]\n",
    "location_stats_less_than_10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "1e3c7d56",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1293"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(df5.location.unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "81bce716",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "242"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df5.location=df5.location.apply(lambda x:'other' if x in location_stats_less_than_10 else x)\n",
    "len(df5.location.unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "75036bc6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "      <th>price_per_sqft</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Electronic City Phase II</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1056.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>39.07</td>\n",
       "      <td>2</td>\n",
       "      <td>3699.810606</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Chikka Tirupathi</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>2600.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>120.00</td>\n",
       "      <td>4</td>\n",
       "      <td>4615.384615</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Uttarahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1440.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>62.00</td>\n",
       "      <td>3</td>\n",
       "      <td>4305.555556</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Lingadheeranahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1521.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>95.00</td>\n",
       "      <td>3</td>\n",
       "      <td>6245.890861</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kothanur</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1200.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>51.00</td>\n",
       "      <td>2</td>\n",
       "      <td>4250.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Whitefield</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1170.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>38.00</td>\n",
       "      <td>2</td>\n",
       "      <td>3247.863248</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Old Airport Road</td>\n",
       "      <td>4 BHK</td>\n",
       "      <td>2732.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>204.00</td>\n",
       "      <td>4</td>\n",
       "      <td>7467.057101</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Rajaji Nagar</td>\n",
       "      <td>4 BHK</td>\n",
       "      <td>3300.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>600.00</td>\n",
       "      <td>4</td>\n",
       "      <td>18181.818182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Marathahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1310.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>63.25</td>\n",
       "      <td>3</td>\n",
       "      <td>4828.244275</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>other</td>\n",
       "      <td>6 Bedroom</td>\n",
       "      <td>1020.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>370.00</td>\n",
       "      <td>6</td>\n",
       "      <td>36274.509804</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   location       size  total_sqft  bath   price  bhk  \\\n",
       "0  Electronic City Phase II      2 BHK      1056.0   2.0   39.07    2   \n",
       "1          Chikka Tirupathi  4 Bedroom      2600.0   5.0  120.00    4   \n",
       "2               Uttarahalli      3 BHK      1440.0   2.0   62.00    3   \n",
       "3        Lingadheeranahalli      3 BHK      1521.0   3.0   95.00    3   \n",
       "4                  Kothanur      2 BHK      1200.0   2.0   51.00    2   \n",
       "5                Whitefield      2 BHK      1170.0   2.0   38.00    2   \n",
       "6          Old Airport Road      4 BHK      2732.0   4.0  204.00    4   \n",
       "7              Rajaji Nagar      4 BHK      3300.0   4.0  600.00    4   \n",
       "8              Marathahalli      3 BHK      1310.0   3.0   63.25    3   \n",
       "9                     other  6 Bedroom      1020.0   6.0  370.00    6   \n",
       "\n",
       "   price_per_sqft  \n",
       "0     3699.810606  \n",
       "1     4615.384615  \n",
       "2     4305.555556  \n",
       "3     6245.890861  \n",
       "4     4250.000000  \n",
       "5     3247.863248  \n",
       "6     7467.057101  \n",
       "7    18181.818182  \n",
       "8     4828.244275  \n",
       "9    36274.509804  "
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df5.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "e655a071",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "242"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(df5['location'].unique()) #abhi yeh bass aise location haiin joh ke 10 sejyada barr ayee haiiinn aur joh 10 ya osse kam haiinn woh other me chale gayeehaib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "468d4baf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(13246, 7)"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df5.shape\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "321b1be0",
   "metadata": {},
   "source": [
    "# Outlier Analysis\n",
    "As a data scientist when you have a conversation with your business manager (who has expertise in real estate), he will tell you that normally square ft per bedroom is 300 (i.e. 2 bhk apartment is minimum 600 sqft. If you have for example 400 sqft apartment with 2 bhk than that seems suspicious and can be removed as an outlier. We will remove such outliers by keeping our minimum thresold per bhk to be 300 sqft ......"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "d4cd6f50",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "      <th>price_per_sqft</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>other</td>\n",
       "      <td>6 Bedroom</td>\n",
       "      <td>1020.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>370.0</td>\n",
       "      <td>6</td>\n",
       "      <td>36274.509804</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>HSR Layout</td>\n",
       "      <td>8 Bedroom</td>\n",
       "      <td>600.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>200.0</td>\n",
       "      <td>8</td>\n",
       "      <td>33333.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58</th>\n",
       "      <td>Murugeshpalya</td>\n",
       "      <td>6 Bedroom</td>\n",
       "      <td>1407.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>6</td>\n",
       "      <td>10660.980810</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>68</th>\n",
       "      <td>Devarachikkanahalli</td>\n",
       "      <td>8 Bedroom</td>\n",
       "      <td>1350.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>85.0</td>\n",
       "      <td>8</td>\n",
       "      <td>6296.296296</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>70</th>\n",
       "      <td>other</td>\n",
       "      <td>3 Bedroom</td>\n",
       "      <td>500.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>3</td>\n",
       "      <td>20000.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               location       size  total_sqft  bath  price  bhk  \\\n",
       "9                 other  6 Bedroom      1020.0   6.0  370.0    6   \n",
       "45           HSR Layout  8 Bedroom       600.0   9.0  200.0    8   \n",
       "58        Murugeshpalya  6 Bedroom      1407.0   4.0  150.0    6   \n",
       "68  Devarachikkanahalli  8 Bedroom      1350.0   7.0   85.0    8   \n",
       "70                other  3 Bedroom       500.0   3.0  100.0    3   \n",
       "\n",
       "    price_per_sqft  \n",
       "9     36274.509804  \n",
       "45    33333.333333  \n",
       "58    10660.980810  \n",
       "68     6296.296296  \n",
       "70    20000.000000  "
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df5[df5.total_sqft/df5.bhk<300].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "6bef2d4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200.0"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Outlier Analysis....\n",
    "1200/6 # not ohk becoz bhai 1200sqft main 6 kamre kaise ayengee"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "0d8a65e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "600.0"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1200/2 # 1200 me doo kamre aa sakte haiinnn \n",
    "\n",
    "# Check above data points. \n",
    "# We have 6 bhk apartment with 1020 sqft. Another one is 8 bhk and total sqft is 600. \n",
    "# These are clear data errors that can be removed safely"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "4d72e62c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df6 = df5[~(df5.total_sqft / df5.bhk < 300)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "3453b8eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(12502, 7)"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df6.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "8a36543f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "      <th>price_per_sqft</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Electronic City Phase II</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1056.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>39.07</td>\n",
       "      <td>2</td>\n",
       "      <td>3699.810606</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Chikka Tirupathi</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>2600.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>120.00</td>\n",
       "      <td>4</td>\n",
       "      <td>4615.384615</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Uttarahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1440.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>62.00</td>\n",
       "      <td>3</td>\n",
       "      <td>4305.555556</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Lingadheeranahalli</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1521.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>95.00</td>\n",
       "      <td>3</td>\n",
       "      <td>6245.890861</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kothanur</td>\n",
       "      <td>2 BHK</td>\n",
       "      <td>1200.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>51.00</td>\n",
       "      <td>2</td>\n",
       "      <td>4250.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   location       size  total_sqft  bath   price  bhk  \\\n",
       "0  Electronic City Phase II      2 BHK      1056.0   2.0   39.07    2   \n",
       "1          Chikka Tirupathi  4 Bedroom      2600.0   5.0  120.00    4   \n",
       "2               Uttarahalli      3 BHK      1440.0   2.0   62.00    3   \n",
       "3        Lingadheeranahalli      3 BHK      1521.0   3.0   95.00    3   \n",
       "4                  Kothanur      2 BHK      1200.0   2.0   51.00    2   \n",
       "\n",
       "   price_per_sqft  \n",
       "0     3699.810606  \n",
       "1     4615.384615  \n",
       "2     4305.555556  \n",
       "3     6245.890861  \n",
       "4     4250.000000  "
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df6.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e80b3f7",
   "metadata": {},
   "source": [
    "# Outlier Removal Using Standard Deviation and Mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "9130c473",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     12456.000000\n",
       "mean       6308.502826\n",
       "std        4168.127339\n",
       "min         267.829813\n",
       "25%        4210.526316\n",
       "50%        5294.117647\n",
       "75%        6916.666667\n",
       "max      176470.588235\n",
       "Name: price_per_sqft, dtype: float64"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df6.price_per_sqft.describe() # mathematical function deta haiinn.....\n",
    "#yeh batara ke kamse kamm 267sqft me yaa jyada se jyada 176470sqft \n",
    "# but jyada wala possible nahi haiin toh kam waale he thhek hain"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "40d918a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10241, 7)"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def remove_pps_outlier(df):\n",
    "    df_out = pd.DataFrame()\n",
    "    for key, subdf in df.groupby('location'):\n",
    "        m = np.mean(subdf['price_per_sqft'])\n",
    "        st = np.std(subdf['price_per_sqft'])\n",
    "        reduced_df = subdf[(subdf['price_per_sqft'] > (m - st)) & (subdf['price_per_sqft'] <= (m + st))]\n",
    "        df_out = pd.concat([df_out, reduced_df], ignore_index=True)\n",
    "    return df_out\n",
    "\n",
    "df7=remove_pps_outlier(df6)\n",
    "df7.shape\n",
    "     "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "acb3cfcb",
   "metadata": {},
   "source": [
    "Let's check if for a given location how does the 2 BHK and 3 BHK property prices look like"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "523bb953",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABNYAAANVCAYAAAC09nNHAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQGoP6dpAAB4K0lEQVR4nOzdeXTddZ0//udNk9RwQ8LaTToVFUexoAjzFWip7MiIFOoMCOOCy+8L04JA6agVFetCAbFVj7a4DajoF8eBgoyCoAhSkBkEFEFGxWFTuiiUhFxC0yb390emoaFbcps9j8c59+SzvD+fvD7lQ07OM++lUC6XywEAAAAAeqVqsAsAAAAAgOFIsAYAAAAAFRCsAQAAAEAFBGsAAAAAUAHBGgAAAABUQLAGAAAAABUQrAEAAABABQRrAAAAAFABwRoAAAAAVECwBgDQB6644ooUCoWuT3V1dSZOnJi3v/3t+cMf/lDxfV/2spfltNNO65NrH3300RQKhVxxxRVbvW5Du0KhkKuuumqT85/4xCdSKBTy17/+taK6AABGiurBLgAAYCS5/PLL8+pXvzrPP/987rjjjnzmM5/Jz372s/z3f/93dt55517fb9myZWloaKiolhdfO3HixPziF7/IK17xih7f4/zzz8/b3va21NTUVFQDAMBIpscaAEAfmjp1ag488MAceuihOf/88/PhD384q1evzrXXXlvR/fbbb79eBWFbu3bs2LE58MADs/vuu/fo+mOPPTb/8z//k8suu6yi7z+YnnvuucEuAQAYBQRrAAD96IADDkiSrFq1quvY888/n/POOy+vf/3r09jYmF122SUHHXRQrrvuuk2uf/Fwzu25tqdDQTc4/PDDc8wxx+RTn/pUnn322a22vfnmmzNz5szsscceeclLXpJXvvKVOf300zc7XPS6667Lvvvum7Fjx+blL395vvCFL3QNL93Yl7/85cyYMSPjxo1LsVjMPvvsk0suuSTr1q3r1u7QQw/N1KlT8/Of/zwHH3xwdthhh7z3ve/t0TMCAGwPQ0EBAPrRI488kiR51ate1XVs7dq1efrppzNv3ry89KUvTVtbW37yk59k1qxZufzyy/Oud71ri/fbnmsrcfHFF2e//fbLZz/72Xzyk5/cYrs//vGPOeigg/L+978/jY2NefTRR7No0aJMnz49v/nNb7qGkt54442ZNWtWZsyYke9973tZv359Lr300m7B48b3PPXUU7PnnnumtrY2v/71r/OZz3wm//3f/51//dd/7dZ2xYoVecc73pEPfvCDufDCC1NV5e/HAED/E6wBAPSh9vb2rF+/vmuOtU9/+tOZMWNGjj/++K42jY2Nufzyy7tdc8QRR2TNmjX5/Oc/v9VwbHuurcTrXve6nHrqqVm0aFFmz56dCRMmbLbdGWec0bVdLpdz8MEH59BDD82UKVNyww03dD3/xz/+8bz0pS/Nj3/849TW1iZJ3vzmN+dlL3vZJvdctGhR13ZHR0cOOeSQ7LrrrnnPe96Tz33uc93mrHv66afz/e9/P4cffnhfPDYAQI/4Ux4AQB868MADU1NTkx133DFvfvObs/POO+e6665LdXX3v2d+//vfz7Rp01JfX5/q6urU1NTkG9/4Rh566KFtfo/tubYSn/70p7Nu3bosWLBgi21Wr16dM844I5MnT+6qacqUKUnSVVepVMovf/nLnHDCCV2hWpLU19fnrW996yb3vO+++3L88cdn1113zZgxY1JTU5N3vetdaW9vz+9///tubXfeeWehGgAw4ARrAAB96Fvf+lbuvvvu3HLLLTn99NPz0EMP5ZRTTunW5pprrslJJ52Ul770pbnyyivzi1/8InfffXfe+9735vnnn9/q/bfn2kq97GUvy+zZs/P1r389f/jDHzY539HRkaOPPjrXXHNNPvjBD+anP/1p/uu//it33XVXkqS1tTVJsmbNmpTL5YwfP36Te7z42OOPP55DDjkkf/7zn/OFL3wht99+e+6+++58+ctf7nbPDSZOnNgnzwoA0BuGggIA9KHXvOY1XQsWHHbYYWlvb8/Xv/71/Pu//3v+4R/+IUly5ZVXZs8998z3vve9bhP2r127dpv3355rt8dHP/rR/Ou//ms+8pGP5LWvfW23cw888EB+/etf54orrsi73/3uruMPP/xwt3Y777xzCoXCZudTW7lyZbf9a6+9NqVSKddcc01Xz7ck+dWvfrXZ+l688AEAwEDQYw0AoB9dcskl2XnnnfPxj388HR0dSTpDoNra2m5h0MqVKze7sueLbc+122PXXXfNhz70ofz7v/97/uu//muTmpJk7Nix3Y5/5Stf6bZfLBZzwAEH5Nprr01bW1vX8ZaWlvzHf/zHNu9ZLpfzta99bfsfBgCgjwjWAAD60c4775z58+fnoYceyne/+90kyXHHHZff/e53mT17dm655ZZ885vfzPTp03s0nHF7rt1e55xzTiZNmpQbbrih2/FXv/rVecUrXpEPf/jD+X//7//lxz/+cc4888z84Ac/2OQen/zkJ/PnP/85xxxzTK699tpcffXVOfLII1NfX98tLDzqqKNSW1ubU045JTfccEOWLVuWY445JmvWrOn35wQA6CnBGgBAPzvrrLPyN3/zN/nkJz+Z9vb2vOc978lFF12UG264IX//93+fiy++OB/+8Idz6qmnbvb6jQOn7bl2e+2www75xCc+scnxmpqaXH/99XnVq16V008/PaecckpWr16dn/zkJ5u0ffOb35yrr746Tz31VE4++eTMnTs3J554YmbOnJmddtqpq92rX/3qXH311VmzZk1mzZqVs846K69//evzxS9+sc+eBwBgexXK5XJ5sIsAAGDzdtlll7z3ve/NpZdeOqDXDqR169bl9a9/fV760pfmpptuGuxyAAB6zOIFAABD0P33358f/ehHWbNmTQ466KABu3YgvO9978tRRx2ViRMnZuXKlbnsssvy0EMP5Qtf+MJglwYA0CuCNQCAIejss8/Of//3f2fevHmZNWvWgF07EJ599tnMmzcvf/nLX1JTU5M3vOEN+dGPfpQjjzxysEsDAOgVQ0EBAAAAoAIWLwAAAACACgjWAAAAAKACgjUAAAAAqIDFC5J0dHTkySefzI477phCoTDY5QAAAAAwSMrlcp599tlMmjQpVVVb75MmWEvy5JNPZvLkyYNdBgAAAABDxBNPPJE99thjq20Ea0l23HHHJJ3/YA0NDYNcDQAAAACDpbm5OZMnT+7Ki7ZGsJZ0Df9saGgQrAEAAADQo+nCLF4AAAAAABUQrAEAAABABQRrAAAAAFABc6z1ULlczvr169Pe3j7YpYxYY8aMSXV1dY/GMAMAAAAMNsFaD7S1tWXFihV57rnnBruUEW+HHXbIxIkTU1tbO9ilAAAAAGyVYG0bOjo68sgjj2TMmDGZNGlSamtr9ajqB+VyOW1tbfnLX/6SRx55JHvttVeqqoxUBgAAAIYuwdo2tLW1paOjI5MnT84OO+ww2OWMaHV1dampqcljjz2Wtra2vOQlLxnskgAAAAC2SJegHtJ7amD4dwYAAACGCykGAAAAAFRAsAYAAAAAFRCsAQAAAEAFBGsDqLU1WbWq82t/W7hwYf7u7/4uO+64Y8aNG5cTTjghv/vd77Z6zRVXXJFCodD1qa+vz/77759rrrmmW7tDDz0055xzzmav32mnnba4nyQPPfRQ9thjj8yaNStr166t9PEAAAAABp1gbQAsX57MmpXU1ycTJnR+nTUrueOO/vuet912W+bMmZO77rorN998c9avX5+jjz46pVJpq9c1NDRkxYoVWbFiRe67774cc8wxOemkk7YZyvXE3XffnUMOOSTHHHNMvv/972fs2LHbfU8AAACAwSJY62dLlyYzZiTXX590dHQe6+jo3D/kkOSyy/rn+95444057bTT8trXvjave93rcvnll+fxxx/PPffcs9XrCoVCJkyYkAkTJmSvvfbKpz/96VRVVeX+++/frnpuueWWHH744XnPe96Tb3zjGxkzZsx23Q8AAABgsAnW+tHy5cmcOUm5nKxf3/3c+vWdx2fP7t+eaxs0NTUlSXbZZZceX9Pe3p5vfvObSZI3vOENFX/vZcuW5S1veUvOP//8fPazn634PgAAAABDSfVgFzCSLVqUjBmzaai2sTFjksWLk2nT+q+OcrmcuXPnZvr06Zk6depW2zY1NaW+vj5J0trampqamnz1q1/NK17xim7tlixZkq9//evdjq1fvz4veclLuh1raWnJP/7jP+YjH/lIPvzhD/fB0wAAAAAMDYK1ftLamlx33QvDP7dk/fpk2bLO9nV1/VPLmWeemfvvvz/Lly/fZtsdd9wx9957b5Lkueeey09+8pOcfvrp2XXXXfPWt761q90//dM/5fzzz+927TXXXJMLL7yw27G6urpMnz49X/va13LKKafkNa95TR88EQAAAMDgE6z1k+bmbYdqG3R0dLbvj2DtrLPOyg9+8IP8/Oc/zx577LHN9lVVVXnlK1/Ztb/vvvvmpptuysUXX9wtWGtsbOzWLknGjRu3yf3GjBmTa6+9Nm9729ty2GGH5ZZbbsnee++9HU8EAAAAMDSYY62fNDQkVT38162q6mzfl8rlcs4888xcc801ueWWW7LnnntWfK8xY8aktbW14uvHjh2ba665Jv/n//yfHHbYYXnggQcqvhcAAADAUCFY6yd1dcnMmUn1NvoEVlcnJ57Y973V5syZkyuvvDLf/e53s+OOO2blypVZuXLlNgOycrnc1faRRx7JV7/61fz4xz/OzJkzt6ue2traXH311Tn44INz+OGH5ze/+c123Q8AAABgsAnW+tHcuUl7+9bbtLcn557b99976dKlaWpqyqGHHpqJEyd2fb73ve9t9brm5uautq95zWvyuc99Lp/85Cc3mU+tEjU1Nfm3f/u3zJgxI4cffnjuv//+7b4nAAAAwGAplMvl8mAXMdiam5vT2NiYpqamNLxoTObzzz+fRx55JHvuuecmK172xGWXJbNnb7o6aHV1Z6i2ZElyxhnb+wQjx/b+ewMAAABsj63lRC+mx1o/O+OM5PbbO4eFbphzraqqc//224VqAAAAAMOVVUEHwLRpnZ/W1s7VPxsa+mcFUAAAAAAGjmBtANXVCdQAAAAARgpDQQEAAACgAoI1AAAAAKiAYA0AAABglCi1lVJYUEhhQSGlttJglzPsCdYAAAAAoAKCNQAAAACogFVBAQAAAEawjYd8ltZtfjtJirXFAatppBCsAQAAAIxg9QvrN3t8/KXju+2XLygPRDkjiqGgI9TSpUuz7777pqGhIQ0NDTnooINyww03bPWaK664IoVCoetTX1+f/fffP9dcc023doceemjOOeeczV6/0047bXE/SR566KHssccemTVrVtauXVvp4wEAAAAMOj3WBkiprdSVELfMb+n37pV77LFHLrroorzyla9Mknzzm9/MzJkzc9999+W1r33tFq9raGjI7373uyTJs88+m8svvzwnnXRSHnzwwfzt3/7tdtV0991359hjj83MmTPz1a9+NWPGjNmu+wEAAADb1jK/pWu7tK7U1VNt1bxVKdYY/rk99Fgbod761rfm7//+7/OqV70qr3rVq/KZz3wm9fX1ueuuu7Z6XaFQyIQJEzJhwoTstdde+fSnP52qqqrcf//921XPLbfcksMPPzzvec978o1vfEOoBgAAAAOkWFt84bNRkFasKXY7R+8J1kaB9vb2XHXVVSmVSjnooIN6dd03v/nNJMkb3vCGir//smXL8pa3vCXnn39+PvvZz1Z8HwAAAIChxFDQfjTYq2785je/yUEHHZTnn38+9fX1WbZsWfbee++tXtPU1JT6+s4hq62trampqclXv/rVvOIVr+jWbsmSJfn617/e7dj69evzkpe8pNuxlpaW/OM//mM+8pGP5MMf/nAfPBUAAADA0CBY60eDverG3/7t3+ZX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+c1vzooVK7o+P/rRj7rd45xzzsmyZcty1VVXZfny5Wlpaclxxx2X9vb2gX4cAAAAAEaR6sH85m9961u77X/mM5/J0qVLc9ddd+W1r31tkmTs2LGZMGHCZq9vamrKN77xjXz729/OkUcemSS58sorM3ny5PzkJz/JMccc078PAAAAALAdNh7yWVq3+e0kKdYWB6wmem5Qg7WNtbe35/vf/35KpVIOOuigruO33nprxo0bl5122ilvetOb8pnPfCbjxo1Lktxzzz1Zt25djj766K72kyZNytSpU3PnnXduMVhbu3Zt1q5d27Xf3NzcT08FAAAAsGX1C+s3e3z8peO77ZcvKA9EOfTSoC9e8Jvf/Cb19fUZO3ZszjjjjCxbtix77713kuTYY4/Nd77zndxyyy353Oc+l7vvvjuHH354Vyi2cuXK1NbWZuedd+52z/Hjx2flypVb/J4LFy5MY2Nj12fy5Mn994AAAAAAjEiD3mPtb//2b/OrX/0qzzzzTK6++uq8+93vzm233Za99947J598cle7qVOn5oADDsiUKVPywx/+MLNmzdriPcvlcgqFwhbPz58/P3Pnzu3ab25uFq4BAAAAA65lfkvXdmldqaun2qp5q1KsMfxzqBv0YK22tjavfOUrkyQHHHBA7r777nzhC1/IV77ylU3aTpw4MVOmTMkf/vCHJMmECRPS1taWNWvWdOu1tnr16hx88MFb/J5jx47N2LFj+/hJAAAAAHpnS3OnFWuK5lUbBgZ9KOiLlcvlbvOfbeypp57KE088kYkTJyZJ9t9//9TU1OTmm2/uarNixYo88MADWw3WAAAAAGB7DWqPtY985CM59thjM3ny5Dz77LO56qqrcuutt+bGG29MS0tLPvGJT+Rtb3tbJk6cmEcffTQf+chHsttuu+XEE09MkjQ2NuZ973tfzjvvvOy6667ZZZddMm/evOyzzz5dq4QCAAAAQH8Y1GBt1apVeec735kVK1aksbEx++67b2688cYcddRRaW1tzW9+85t861vfyjPPPJOJEyfmsMMOy/e+973suOOOXfdYvHhxqqurc9JJJ6W1tTVHHHFErrjiiowZM2YQnwwAAACgd4q1Rat/DjOFcrk86v+LNTc3p7GxMU1NTWloaBjscgAAAAAYJL3JiYbcHGsAAAAAMBwI1gAAAACgAoI1AAAAAKiAYA0AAAAAKiBYAwAAAIAKCNYAAAAAoAKCNQAAAACogGANAAAAACogWAMAAACACgjWAAAAAKACgjUAAAAAqIBgDQAAAEapUlsphQWFFBYUUmorDXY5o57/HsOPYA0AAAAAKiBYAwAAAIAKVA92AQAAAMDA2XiIYWnd5reTpFhbHLCaRjP/PYa3QrlcLg92EYOtubk5jY2NaWpqSkNDw2CXAwAAAP2msKDQo3blC0Z9XDAg/PcYenqTExkKCgAAAAAVMBQUAAAARpGW+S1d26V1pYy/dHySZNW8VSnWGG440Pz3GN4EawAAADCKbGmurmJN0Txeg8B/j+HNUFAAAAAAqIBgDQAAAAAqYCgoAAAAjFLF2qLVJocQ/z2GHz3WAAAAAKACgjUAAAAAqIBgDQAAAAAqIFgDAAAAeqXUVkphQSGFBYWU2kqDXQ4MGsEaAAAAAFRAsAYAAAAAFage7AIAAACAoW/jIZ+ldZvfTpJibXHAaoLBJlgDAAAAtql+Yf1mj4+/dHy3/fIF5YEoB4YEQ0EBAAAAoAJ6rAEAAADb1DK/pWu7tK7U1VNt1bxVKdYY/snoJFgDAAAAtmlLc6cVa4rmVWPUMhQUAAAAACogWAMAAACAChgKCgAAAPRKsbY4rFf/LLWVulY5bZnfYigrFdNjDQAAAAAqIFgDAAAAgAoYCgoAAACMeKW20gvb6za/nWx59VPYHMEaAAAAMOJtmFPtxcZfOr7b/nCeO46BZygoAAAAAFRAjzUAAABgxGuZ39K1XVpX6uqptmreqhRrDP+kMoI1AAAAYMTb0txpxZqiedWomKGgAAAAAFABwRoAAAAAVMBQUAAAAGBUKdYWrf5Jn9BjDQAAAAAqIFgDAAAAgAoI1gAAAACgAoI1AAAAAKiAYA0AAAAAKiBYAwAAAIAKCNYAAAAAoAKCNQAAAACogGANAAAAACogWAMAAACACgjWAAAAAKACgjUAAAAAqIBgDQAAAEapUlsphQWFFBYUUmorDXY5MOwI1gAAAACgAoI1AAAAAKhA9WAXAAAAAAycjYd8ltZtfjtJirXFAasJhivBGgAAAIwi9QvrN3t8/KXju+2XLygPRDkwrBkKCgAAAAAV0GMNAAAARpGW+S1d26V1pa6eaqvmrUqxxvBP6A3BGgAAAIwiW5o7rVhTNK8a9JKhoAAAAABQAcEaAAAAAFTAUFAAAAAYpYq1Rat/wnbQYw0AAAAAKiBYAwAAAIAKCNYAAAAAoAKCNQAAAACogGANAAAAACogWAMAAACACgjWAAAAAKACgjUAAAAAqEB1bxo3NTVl2bJluf322/Poo4/mueeey+6775799tsvxxxzTA4++OD+qhMAAAAAhpQe9VhbsWJF/r//7//LxIkT88lPfjKlUimvf/3rc8QRR2SPPfbIz372sxx11FHZe++9873vfa+/awYAAACAQdejHmuve93r8q53vSv/9V//lalTp262TWtra6699tosWrQoTzzxRObNm9enhQIAAADAUFIol8vlbTX6y1/+kt13373HN+1t+8HW3NycxsbGNDU1paGhYbDLAQAAAGCQ9CYn6tFQ0N6GZMMpVAMAAACASvR6VdBvfvOb+eEPf9i1/8EPfjA77bRTDj744Dz22GN9WhwAAAAADFW9DtYuvPDC1NXVJUl+8Ytf5Etf+lIuueSS7Lbbbjn33HP7vEAAAAAAGIp6tHjBxp544om88pWvTJJce+21+Yd/+If83//7fzNt2rQceuihfV0fAAAAAAxJve6xVl9fn6eeeipJctNNN+XII49MkrzkJS9Ja2tr31YHAAAAAENUr3usHXXUUXn/+9+f/fbbL7///e/zlre8JUny4IMP5mUve1lf1wcAAAAAQ1Kve6x9+ctfzkEHHZS//OUvufrqq7PrrrsmSe65556ccsopfV4gAAAAAAxFhXK5XB7sIgZbc3NzGhsb09TUlIaGhsEuBwAAAIBB0pucqNc91pLk9ttvzzve8Y4cfPDB+fOf/5wk+fa3v53ly5dXcjsAAAAAGHZ6HaxdffXVOeaYY1JXV5d77703a9euTZI8++yzufDCC/u8QAAAAAAYinodrH3605/OZZddlq997WupqanpOn7wwQfn3nvv7dPiAAAAAGCo6nWw9rvf/S4zZszY5HhDQ0OeeeaZvqgJAAAAAIa8XgdrEydOzMMPP7zJ8eXLl+flL395nxQFAAAAAENdr4O1008/PWeffXb+8z//M4VCIU8++WS+853vZN68eZk9e3Z/1AgAAAAAQ051by/44Ac/mKamphx22GF5/vnnM2PGjIwdOzbz5s3LmWee2R81AgAAAMCQUyiXy+VKLnzuuefy29/+Nh0dHdl7771TX1/f17UNmObm5jQ2NqapqSkNDQ2DXQ4AAAAAg6Q3OVGvh4Ju8OSTT+app57KPvvsk/r6+lSYzwEAAADAsNTrYO2pp57KEUcckVe96lX5+7//+6xYsSJJ8v73vz/nnXdenxcIAAAAAENRr4O1c889NzU1NXn88cezww47dB0/+eSTc+ONN/ZpcQAAAAAwVPV68YKbbropP/7xj7PHHnt0O77XXnvlscce67PCAAAAAGAo63WPtVKp1K2n2gZ//etfM3bs2D4pCgAAAACGul4HazNmzMi3vvWtrv1CoZCOjo589rOfzWGHHdanxQEAAADAUNXroaCf/exnc+ihh+aXv/xl2tra8sEPfjAPPvhgnn766dxxxx39USMAAAAADDm97rG299575/7778//+T//J0cddVRKpVJmzZqV++67L694xSv6o0YAAAAAGHIK5XK5PNhFDLbm5uY0NjamqakpDQ0Ng10OAAAAAIOkNzlRr3usJcmaNWty6aWX5n3ve1/e//7353Of+1yefvrpXt9n6dKl2XfffdPQ0JCGhoYcdNBBueGGG7rOl8vlfOITn8ikSZNSV1eXQw89NA8++GC3e6xduzZnnXVWdttttxSLxRx//PH505/+VMljAQAAAECP9TpYu+2227Lnnnvmi1/8YtasWZOnn346X/ziF7Pnnnvmtttu69W99thjj1x00UX55S9/mV/+8pc5/PDDM3PmzK7w7JJLLsmiRYvypS99KXfffXcmTJiQo446Ks8++2zXPc4555wsW7YsV111VZYvX56WlpYcd9xxaW9v7+2jAQAAAECP9Xoo6NSpU3PwwQdn6dKlGTNmTJKkvb09s2fPzh133JEHHnhguwraZZdd8tnPfjbvfe97M2nSpJxzzjn50Ic+lKSzd9r48eNz8cUX5/TTT09TU1N23333fPvb387JJ5+cJHnyySczefLk/OhHP8oxxxzTo+9pKCgAAAAAST8PBf3jH/+Y8847rytUS5IxY8Zk7ty5+eMf/9j7av9Xe3t7rrrqqpRKpRx00EF55JFHsnLlyhx99NFdbcaOHZs3velNufPOO5Mk99xzT9atW9etzaRJkzJ16tSuNpuzdu3aNDc3d/sAAAAAQG/0Olh7wxvekIceemiT4w899FBe//rX97qA3/zmN6mvr8/YsWNzxhlnZNmyZdl7772zcuXKJMn48eO7tR8/fnzXuZUrV6a2tjY777zzFttszsKFC9PY2Nj1mTx5cq/rBgAAAGB0q+7tBR/4wAdy9tln5+GHH86BBx6YJLnrrrvy5S9/ORdddFHuv//+rrb77rvvNu/3t3/7t/nVr36VZ555JldffXXe/e53d5urrVAodGtfLpc3OfZi22ozf/78zJ07t2u/ublZuAYAAABAr/Q6WDvllFOSJB/84Ac3e65QKHQFWz1ZQKC2tjavfOUrkyQHHHBA7r777nzhC1/omldt5cqVmThxYlf71atXd/VimzBhQtra2rJmzZpuvdZWr16dgw8+eIvfc+zYsRk7dmwPnhYAAAAANq/XwdojjzzSH3V0KZfLWbt2bfbcc89MmDAhN998c/bbb78kSVtbW2677bZcfPHFSZL9998/NTU1ufnmm3PSSSclSVasWJEHHnggl1xySb/WCQAAAMDo1utgbcqUKX32zT/ykY/k2GOPzeTJk/Pss8/mqquuyq233pobb7wxhUIh55xzTi688MLstdde2WuvvXLhhRdmhx12yKmnnpokaWxszPve976cd9552XXXXbPLLrtk3rx52WeffXLkkUf2WZ0AAAAA8GK9Dta+9a1vbfX8u971rh7fa9WqVXnnO9+ZFStWpLGxMfvuu29uvPHGHHXUUUk6h5u2trZm9uzZWbNmTd74xjfmpptuyo477th1j8WLF6e6ujonnXRSWltbc8QRR+SKK67otmopAAAAAPS1QrlcLvfmghevwLlu3bo899xzqa2tzQ477JCnn366TwscCM3NzWlsbExTU1MaGhoGuxwAAAAABklvcqKq3t58zZo13T4tLS353e9+l+nTp+f//b//V3HRAAAAADCc9DpY25y99torF110Uc4+++y+uB0AAAAADHl9EqwlyZgxY/Lkk0/21e0AAAAAYEjr9eIFP/jBD7rtl8vlrFixIl/60pcybdq0PisMAAAAAIayXgdrJ5xwQrf9QqGQ3XffPYcffng+97nP9VVdAAAAADCk9TpY6+jo6I86AAAAAGBY6bM51q655prsu+++fXU7AAAAABjSehWsfe1rX8s//uM/5tRTT81dd92VJLnllluy33775R3veEcOOuigfikSAAAAAIaaHgdrl156aebMmZNHHnkk1113XY444ohceOGFOemkk3LCCSfk8ccfz1e+8pX+rBUAAAAAhowez7H2jW98I5dddlne+9735tZb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f/9v3v3ud2fs2LH9WjQADGeltlLqF9YnSVrmt6RYWxzkigAAgEoUyuVyuTcXlMvl3H///Xn00UfT2tqa3XbbLa9//euz22679VeN/a65uTmNjY1pamrS2w6AfidYAwCAoas3OVGPVwXdoFAo5HWve11e97rXVVwgAAAAAAx3vQ7WAIDeK7W9sAhQad3mt5PovTZC6JUIADA69Gjxgv6ycOHC/N3f/V123HHHjBs3LieccEJ+97vfdWtz2mmnpVAodPsceOCB3dqsXbs2Z511VnbbbbcUi8Ucf/zx+dOf/jSQjwIAW1W/sL7rM/7S8V3Hx186vts5AABg+BjUYO22227LnDlzctddd+Xmm2/O+vXrc/TRR6dU6v7X+ze/+c1ZsWJF1+dHP/pRt/PnnHNOli1blquuuirLly9PS0tLjjvuuLS3tw/k4wAAAAAwigzqUNAbb7yx2/7ll1+ecePG5Z577smMGTO6jo8dOzYTJkzY7D2ampryjW98I9/+9rdz5JFHJkmuvPLKTJ48OT/5yU9yzDHH9N8DAEAPtcxv6dourSt19VpbNW9VijWGCY4EhvsCAIw+FQdrDz/8cP74xz9mxowZqaurS7lcTqFQ2K5impqakiS77LJLt+O33nprxo0bl5122ilvetOb8pnPfCbjxo1Lktxzzz1Zt25djj766K72kyZNytSpU3PnnXduNlhbu3Zt1q5d27Xf3Ny8XXUDwLZsKUwp1hQFLSPElobybjz0N0nKF/RqQXYAAIawXg8Ffeqpp3LkkUfmVa96Vf7+7/8+K1asSJK8//3vz3nnnVdxIeVyOXPnzs306dMzderUruPHHntsvvOd7+SWW27J5z73udx99905/PDDu4KxlStXpra2NjvvvHO3+40fPz4rV67c7PdauHBhGhsbuz6TJ0+uuG4AAAAARqde91g799xzU11dnccffzyvec1ruo6ffPLJOffcc/O5z32uokLOPPPM3H///Vm+fHm34yeffHLX9tSpU3PAAQdkypQp+eEPf5hZs2Zt8X5b60E3f/78zJ07t2u/ublZuAYAbBfDfQEARp9eB2s33XRTfvzjH2ePPfbodnyvvfbKY489VlERZ511Vn7wgx/k5z//+Sb3fbGJEydmypQp+cMf/pAkmTBhQtra2rJmzZpuvdZWr16dgw8+eLP3GDt2bMaOHVtRrQCwvYq1RcMBRyDDfQEARp9eDwUtlUrZYYcdNjn+17/+tddhVblczplnnplrrrkmt9xyS/bcc89tXvPUU0/liSeeyMSJE5Mk+++/f2pqanLzzTd3tVmxYkUeeOCBLQZrAAAAALC9eh2szZgxI9/61re69guFQjo6OvLZz342hx12WK/uNWfOnFx55ZX57ne/mx133DErV67MypUr09ramiRpaWnJvHnz8otf/CKPPvpobr311rz1rW/NbrvtlhNPPDFJ0tjYmPe9730577zz8tOf/jT33Xdf3vGOd2SfffbpWiUUAAAAAPpaoVwu92osym9/+9sceuih2X///XPLLbfk+OOPz4MPPpinn346d9xxR17xilf0/JtvYQ60yy+/PKeddlpaW1tzwgkn5L777sszzzyTiRMn5rDDDsunPvWpbnOiPf/88/mXf/mXfPe7301ra2uOOOKILFmypMfzpjU3N6exsTFNTU1paGjocf0AAAAAjCy9yYl6HawlnStxLl26NPfcc086Ojryhje8IXPmzOkanjncCNYAAAAASAYgWBtpBGsADKRSWyn1C+uTdK4kaWJ7AAAYOnqTE/V6jrXLL7883//+9zc5/v3vfz/f/OY3e3s7AAAAABiWeh2sXXTRRdltt902OT5u3LhceOGFfVIUAAAAAAx11b294LHHHsuee+65yfEpU6bk8ccf75OiAGCkKbWVXthet/ntJIaFAgDAMNLrYG3cuHG5//7787KXvazb8V//+tfZdddd+6ouABhRNsyp9mLjLx3fbb98waif+hQAAIaNXg8Fffvb354PfOAD+dnPfpb29va0t7fnlltuydlnn523v/3t/VEjAAAAAAw5ve6x9ulPfzqPPfZYjjjiiFRXd17e0dGRd73rXeZYA4AtaJnf0rVdWlfq6qm2at6qFGsM/wQAgOGo18FabW1tvve97+VTn/pUfv3rX6euri777LNPpkyZ0h/1AcCIsKW504o1RfOqAQDAMNXrYG2DV73qVXnVq17Vl7UAAAAAwLDRo2Bt7ty5+dSnPpVisZi5c+dute2iRYv6pDAAGKm6rRDaVtJjDQAAhqkeBWv33Xdf1q1blyS59957UygUNttuS8cBgBdsHKQJ1QZOa2vS3Jw0NCR1dYNdDQAAI0GPgrWf/exnXdu33nprf9UCANDnli9PFi1Krrsu6ehIqqqS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V12V5cuXp6WlJccdd1za29v7u3zS2VNtzpykXE7Wr+9+bv36zuOzZ+u5BgAAAIw81YP5zY899tgce+yxW20zduzYTJgwYbPnmpqa8o1vfCPf/va3c+SRRyZJrrzyykyePDk/+clPcswxx/R5zXS3aFEyZsymodrGxoxJFi9Opk0buLoAttfGQz5L6za/nSTF2uKA1QQAAAwtgxqs9cStt96acePGZaeddsqb3vSmfOYzn8m4ceOSJPfcc0/WrVuXo48+uqv9pEmTMnXq1Nx5551bDNbWrl2btWvXdu03Nzf370OMUK2tyXXXvTD8c0vWr0+WLetsX1c3MLUBbK/6hfWbPT7+0vHd9ssXlAeiHAAAYAga0osXHHvssfnOd76TW265JZ/73Ody99135/DDD+8KxVauXJna2trsvPPO3a4bP358Vq5cucX7Lly4MI2NjV2fyZMn9+tzjFTNzdsO1Tbo6OhsDwAAADBSDOkeayeffHLX9tSpU3PAAQdkypQp+eEPf5hZs2Zt8bpyuZxCobDF8/Pnz8/cuXO79pubm4VrFWhoSKqqehauVVV1tgcYLlrmt3Rtl9aVunqqrZq3KsUawz8BAIAh3mPtxSZOnJgpU6bkD3/4Q5JkwoQJaWtry5o1a7q1W716dcaPH7+5WyTpnLetoaGh24feq6tLZs5MqrcRz1ZXJyeeaBgoMLwUa4svfDYK0oo1xW7nAACA0WtYBWtPPfVUnnjiiUycODFJsv/++6empiY333xzV5sVK1bkgQceyMEHHzxYZY4qc+cm21qAtb09OffcgakHAAAAYKAM6lDQlpaWPPzww137jzzySH71q19ll112yS677JJPfOITedvb3paJEyfm0UcfzUc+8pHstttuOfHEE5MkjY2Ned/73pfzzjsvu+66a3bZZZfMmzcv++yzT9cqofSv6dOTJUuS2bM3XR20urozVFuyxIqgAAAAwMhTKJfLg7ac2a233prDDjtsk+Pvfve7s3Tp0pxwwgm577778swzz2TixIk57LDD8qlPfarbfGjPP/98/uVf/iXf/e5309ramiOOOCJLlizp1Zxpzc3NaWxsTFNTk2GhFbrjjmTx4s7VPzs6OudUO/HEzp5qQjUAAABguOhNTjSowdpQIVjrO62tnat/NjSYUw0AAAAYfnqTEw3pVUEZfurqBGoAAADA6DCs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8/RUT9+tofr7vGCNTZRKpbzuda/Ll770pU3OPffcc7n33nvzsY99LPfee2+uueaa/P73v8/xxx/frd0555yTZcuW5aqrrsry5cvT0tKS4447Lu3t7V1tTj311PzqV7/KjTfemBtvvDG/+tWv8s53vrPfn4/Bs7V3a2PXXntt/vM//zOTJk3a5Jx3i83Z1rv1xz/+MdOnT8+rX/3q3Hrrrfn1r3+dj33sY3nJS17S1ca7xeZs690699xzc+ONN+bKK6/MQw89lHPPPTdnnXVWrrvuuq423i0257bbbsucOXNy11135eabb8769etz9NFHp1QqdbW55JJLsmjRonzpS1/K3XffnQkTJuSoo47Ks88+29XG+8WLbevd8vs8lerJz60N/D5Pb/Tk3RrSv8+XYSuSlJctW7bVNv/1X/9VTlJ+7LHHyuVyufzMM8+Ua2pqyldddVVXmz//+c/lqqqq8o033lgul8vl3/72t+Uk5bvuuqurzS9+8YtykvJ///d/9/2DMORs6d3605/+VH7pS19afuCBB8pTpkwpL168uOucd4ue2Ny7dfLJJ5ff8Y53bPEa7xY9sbl367WvfW35k5/8ZLdjb3jDG8of/ehHy+Wyd4ueW716dTlJ+bbbbiuXy+VyR0dHecKECeWLLrqoq83zzz9fbmxsLF922WXlctn7Rc+8+N3aHL/PU4ktvVt+n2d7be7dGsq/z+uxxnZrampKoVDITjvtlCS55557sm7duhx99NFdbSZNmpSpU6fmzjvvTJL84he/SGNjY974xjd2tTnwwAPT2NjY1YbRp6OjI+985zvzL//yL3nta1+7yXnvFpXo6OjID3/4w7zqVa/KMccck3HjxuWNb3xjtyF93i0qNX369PzgBz/In//855TL5fzsZz/L73//+xxzzDFJvFv0XFNTU5Jkl112SZI88sgjWblyZbd3Z+zYsXnTm97U9V54v+iJF79bW2rj93l6a3Pvlt/n6QsvfreG+u/zgjW2y/PPP58Pf/jDOfXUU9PQ0JAkWblyZWpra7Pzzjt3azt+/PisXLmyq824ceM2ud+4ceO62jD6XHzxxamurs4HPvCBzZ73blGJ1atXp6WlJRdddFHe/OY356abbsqJJ56YWbNm5bbbbkvi3aJyX/ziF7P33ntnjz32SG1tbd785jdnyZIlmT59ehLvFj1TLpcz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4qWXXurzI5I2NjYIDAxEYGAgPvjgA6xbtw5r167FypUrIYSw2L97DRo0SOrzXa2trWZ1srKy8O677yI1NRX+/v6ws7PDhg0bUFpaalZv6NChZusmkwm+vr7YvXt3p+M6OTl1Oy4XFxd4eHh0am/06NHSu9/udTdZaDKZsGbNGkRGRnaqY2tr2+0x79Xe3o6dO3eitrYW1tbWZuV6vR6zZ8+WyuSMOy4uDteuXcPmzZvh6uqKIUOGwN/fX9YjskRERNQ/MLFGREREA46XlxcOHTqE119/XSo7fPgwvLy8pHUbGxu0t7eb7VdSUoK4uDjMmzcPwP/eudabl/r3RKvVoq2tDbdv34aXlxfa2tpw/PhxPPPMMwCAqqoqXL9+Xap/N9FjNBoxZcoUADD7kMHdvgYEBGDx4sVSWU93nAGAj48PMjMzpQ8N3C8fHx8p0dXVRwd8fHxQVVXVKSl3L0vXo6O7764rLy+HlZWVVH7u3DnExMSgvr4eDg4OXfahp3GXlJQgPT0dOp0OAPDHH3/g77//7rZPRERE1L/xUVAiIiIacJKTk7Fjxw5s27YNFy5cQFpaGrKzs/Hee+9Jddzc3FBQUIDa2lo0NDQAADw8PJCdnY2KigqcPHkSr732GkwmU5+OPWPGDGRkZKCsrAw1NTXIyclBSkoKZs6cCXt7e3h6eiI0NBTx8fEoLS1FWVkZ3nrrLSiVSqkNpVKJadOmYf369Th79iyKi4uxatUqs+N4eHjg+PHjyM3Nxfnz5/HRRx/1+NJ/AIiJiYGjoyPCw8NRUlKC6upqFBUVISkpCX/++WefxgoAzz//PPz9/REREYHc3FzU1NTg8OHDWLVqFY4fPw4AWL16NXbu3IlPPvkEZ86cQWVlJTIzM83GZOl6dKTX6zFnzhxMnjwZTz/9tLRERUXByckJ33777X2N28PDA7t27UJlZSVKS0sRExNjdl2IiIho4GFijYiIiAaciIgIbNmyBRs2bIC3tzcyMjJgMBgwY8YMqU5qairy8vLg4uIi3RW2adMmDB8+HAEBAQgLC0NISAh8fHz6dOyQkBB88803mD17Nry8vLB06VKEhISYfa3TYDDAxcUFwcHBiIyMREJCAkaOHGnWzvbt29Ha2go/Pz8kJSVh3bp1ZtsTExMRGRmJ6OhoPPvss6ivrze7e60rTzzxBIqLizF27FhERkbCy8sLixYtwq1bt2TdwaZQKJCTk4OgoCAsWrQIEyZMwPz581FTU4NRo0ZJ52T//v3Iy8vD1KlTMW3aNKSlpcHV1VVqx9L1uNfVq1fx888/IyoqymIfIiMjodfr72vc27dvR0NDA6ZMmYKFCxdi2bJlna4LERERDSwKce/LOYiIiIjoseTm5obly5dj+fLlj7orRERERPQf3rFGREREREREREQkAxNrREREREREREREMvBRUCIiIiIiIiIiIhl4xxoREREREREREZEMTKwRERERERERERHJwMQaERERERERERGRDEysERERERERERERycDEGhERERERERERkQxMrBEREREREREREcnAxBoREREREREREZEMTKwRERERERERERHJ8H8D8ojVyLEA/wAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1500x1000 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def plot_scatter_chart(df,location):\n",
    "    bhk2 = df[(df.location==location) & (df.bhk==2)]\n",
    "    bhk3 = df[(df.location==location) & (df.bhk==3)]\n",
    "    matplotlib.rcParams['figure.figsize'] = (15,10)\n",
    "    plt.scatter(bhk2.total_sqft,bhk2.price,color='blue',label='2 BHK', s=50)\n",
    "    plt.scatter(bhk3.total_sqft,bhk3.price,marker='+', color='green',label='3 BHK', s=50)\n",
    "    plt.xlabel(\"Total Square Feet Area\")\n",
    "    plt.ylabel(\"Price (Lakh Indian Rupees)\")\n",
    "    plt.title(location)\n",
    "    plt.legend()\n",
    "    \n",
    "plot_scatter_chart(df7,\"Rajaji Nagar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "7eb5ff52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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WBuGnp6erFq1Ks8991ytS5n0dt1118yYMSNTpkypdSkAAAAAQxKsbUd/f38effTR1NfXZ+bMmZkyZYqOqlFQKpXS09OTp556Ko8++mj233//1NWZqQwAAACMX4K17ejp6Ul/f39mzZqVXXfdtdblTGpNTU1pbGzMY489lp6enuyyyy61LgkAAABgm7QEDZPuqbHhewYAAAAmCikGAAAAAFRBsAYAAAAAVRCsAQAAAEAVBGtjqLs7WbOm/HO0LV68OK985Suz2267Zdq0aXnTm96Uhx56aMjXXH311SkUCgOPlpaWvOIVr8i11147aNwxxxyTc889d6uvf8ELXrDN50nyy1/+Mvvss0/mzZuXdevWVfvxAAAAAGpOsDYGVq5M5s1LWlqS9vbyz3nzkjvuGL33vP322zN//vzceeedufXWW9Pb25sTTzwxxWJxyNe1trZm1apVWbVqVX7+85/npJNOymmnnbbdUG447rrrrhx11FE56aST8u///u+ZOnXqDt8TAAAAoFYEa6Ns2bJk7tzkhhuS/v7yuf7+8vOjjkquump03vemm27KGWeckZe+9KU55JBD8uUvfzmPP/547rnnniFfVygU0t7envb29uy///75+Mc/nrq6utx33307VM8Pf/jDHHfccXn3u9+dL33pS6mvr9+h+wEAAADUmmBtFK1cmcyfn5RKSW/v4Gu9veXzZ589up1rG3R0dCRJ9thjj2G/pq+vL1/5yleSJH/yJ39S9XsvX748r3/96/PRj340n/rUp6q+DwAAAMB40lDrAiazJUuS+votQ7VN1dcnV1yRzJkzenWUSqUsWLAgRx55ZGbPnj3k2I6OjrS0tCRJuru709jYmM9//vP5oz/6o0Hjli5dmi9+8YuDzvX29maXXXYZdK6rqyt/9md/lo985CP58Ic/PAKfBgAAAGB8EKyNku7u5PrrN07/3Jbe3mT58vL4pqbRqeX9739/7rvvvqxcuXK7Y3fbbbf87Gc/S5I899xz+f73v5/3ve992XPPPfOGN7xhYNyf//mf56Mf/eig11577bW55JJLBp1ramrKkUcemS984Qs5/fTT85KXvGQEPhEAAABA7QnWRkln5/ZDtQ36+8vjRyNYO+ecc/Ltb387P/7xj7PPPvtsd3xdXV1e/OIXDzw/+OCDc8stt+Syyy4bFKy1tbUNGpck06ZN2+J+9fX1ue666/LmN785xx57bH74wx/mwAMP3IFPBAAAADA+WGNtlLS2JnXD/Hbr6srjR1KpVMr73//+XHvttfnhD3+Y/fbbr+p71dfXp7u7u+rXT506Nddee21e9apX5dhjj80DDzxQ9b0AAAAAxgvB2ihpakpOOSVp2E5PYENDcuqpI9+tNn/+/PzzP/9zvv71r2e33XbL6tWrs3r16u0GZKVSaWDso48+ms9//vO5+eabc8opp+xQPVOmTMm3vvWtHHHEETnuuONy//3379D9AAAAAGpNsDaKFixI+vqGHtPXl5x33si/97Jly9LR0ZFjjjkmM2bMGHh84xvfGPJ1nZ2dA2Nf8pKX5B/+4R/yd3/3d1usp1aNxsbG/Nu//Vvmzp2b4447Lvfdd98O3xMAAACgVgqlUqlU6yJqrbOzM21tbeno6EjrZnMyn3/++Tz66KPZb7/9ttjxcjiuuio5++wtdwdtaCiHakuXJmeeuaOfYPLY0e8bAAAAYEcMlRNtTsfaKDvzzGTFivK00A1rrtXVlZ+vWCFUAwAAAJio7Ao6BubMKT+6u8u7f7a2js4OoAAAAACMHcHaGGpqEqgBAAAATBamggIAAABAFQRrAAAAAFAFwRoAAAAAVSn2FFNYVEhhUSHFnmKtyxlzgjUAAAAAqIJgDQAAAACqYFdQAAAAAIZt0ymfxfVbP06S5inNY1ZTrQjWAAAAABi2lsUtWz0//fLpg56XLiqNRTk1ZSroJLVs2bIcfPDBaW1tTWtra1796lfne9/73pCvufrqq1MoFAYeLS0tecUrXpFrr7120Lhjjjkm55577lZf/4IXvGCbz5Pkl7/8ZfbZZ5/Mmzcv69atq/bjAQAAANScjrUxUuwpDiS6XRd2jXo75D777JNLL700L37xi5MkX/nKV3LKKafk5z//eV760pdu83Wtra156KGHkiTPPvtsvvzlL+e0007Lgw8+mD/+4z/eoZruuuuuvO51r8spp5ySz3/+86mvr9+h+wEAAABjr+vCroHj4vriQKfamoVr0tw4+ad/bkrH2iT1hje8IX/6p3+aAw44IAcccEA+8YlPpKWlJXfeeeeQrysUCmlvb097e3v233//fPzjH09dXV3uu+++Harnhz/8YY477ri8+93vzpe+9CWhGgAAAExQzVOaNz42CdKaG5sHXdsZCNZ2An19fbnmmmtSLBbz6le/uqLXfeUrX0mS/Mmf/EnV7798+fK8/vWvz0c/+tF86lOfqvo+AAAAAOOJqaCjqNa7ZNx///159atfneeffz4tLS1Zvnx5DjzwwCFf09HRkZaW8pTV7u7uNDY25vOf/3z+6I/+aNC4pUuX5otf/OKgc729vdlll10Gnevq6sqf/dmf5SMf+Ug+/OEPj8CnAgAAABgfBGujqNa7ZPzxH/9x7r333vz+97/Pt771rbzrXe/K7bffPmS4tttuu+VnP/tZkuS5557L97///bzvfe/LnnvumTe84Q0D4/78z/88H/3oRwe99tprr80ll1wy6FxTU1OOPPLIfOELX8jpp5+el7zkJSP4CQEAAIBaap7SvFPs/rktgrVJbMqUKQObFxx66KG566678o//+I/53Oc+t83X1NXVDbwmSQ4++ODccsstueyyywYFa21tbYPGJcm0adO2uF99fX2uu+66vPnNb86xxx6bH/7wh9vtmgMAAACYCARro2i87ZJRKpWybt26il9XX1+f7u7uqt936tSpufbaa/OWt7wlxx57bH7wgx9k9uzZVd8PAAAAYDwQrI2iba2dtmGXjNH0kY98JK973esya9asPPvss7nmmmty22235aabbhrydaVSKatXr05SXmPt1ltvzc0335yPfexjO1TPlClT8q1vfSunnXZajjvuuPzgBz/IQQcdtEP3BAAAAKglwdoktWbNmrzzne/MqlWr0tbWloMPPjg33XRTTjjhhCFf19nZmRkzZiQpd5rtu++++bu/+7t86EMf2uGaGhsb82//9m85/fTTB8K1gw8+eIfvCwAAAFALhVKptPOuMPe/Ojs709bWlo6OjrS2tg669vzzz+fRRx/Nfvvtt8WOl5Uo9hQHNjPourBr1DvWJqqR+r4BAAAAqjFUTrQ5HWtjZGffJQMAAABgsqmrdQEAAAAAMBEJ1gAAAACgCoI1AAAAAKiCYG2Y7PEwNnzPAAAAwEQhWNuOxsbGJMlzzz1X40p2Dhu+5w3fOwAAAMB4ZVfQ7aivr88LXvCCrF27Nkmy6667plAo1LiqyadUKuW5557L2rVr84IXvCD19fW1LgkAAABgSIK1YWhvb0+SgXCN0fOCF7xg4PsGAAAAGM8Ea8NQKBQyY8aMTJs2LevXr691OZNWY2OjTjUAAABgwhCsVaC+vl7w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qJBiT7HW5UxqgjUAAAAAqIJgDQAAAACq0FDrAgAAAADYMZtO+Syu3/pxkjRPaR6zmnYGgjUAAACACa5lcctWz0+/fPqg56WLSmNRzk7DVFAAAAAAqIKONQAAAIAJruvCroHj4vriQKfamoVr0txo+udoEawBAAAATHDbWjutubHZumqjyFRQAAAAAKiCYA0AAAAAqmAqKAAAAMAk0jyl2e6fY0THGgAAAABUQbAGAAAAAFUQrAEAAABAFQRrAAAAAFAFwRoAAAAAVEGwBgAAAABVEKwBAAAAQBUEawAAAABQBcEaAAAAAFRBsAYAAAAAVRCsAQAAAEAVBGsAAAAAUAXBGgAAAABUQbAGAAAAAFUQrAEAADVR7CmmsKiQwqJCij3FWpcDABUTrAEAAABAFWoarC1evDivfOUrs9tuu2XatGl505velIceemjQmDPOOCOFQmHQ4/DDDx80Zt26dTnnnHOy1157pbm5OW984xvz61//eiw/CgAAAAA7mZoGa7fffnvmz5+fO++8M7feemt6e3tz4oknplgc3Ab+2te+NqtWrRp4fPe73x10/dxzz83y5ctzzTXXZOXKlenq6srJJ5+cvr6+sfw4AADAdhR7ihsf6zf+7/7i+uKgawAwERRKpVKp1kVs8NRTT2XatGm5/fbbM3fu3CTljrXf//73ue6667b6mo6Ojuy999752te+lre+9a1JkieffDKzZs3Kd7/73Zx00klbvGbdunVZt27dwPPOzs7MmjUrHR0daW1tHfkPBgAAJEkKiwrDGle6aNz83xQAdjKdnZ1pa2sbVk40rtZY6+joSJLsscceg87fdtttmTZtWg444ID81V/9VdauXTtw7Z577sn69etz4oknDpybOXNmZs+enZ/85CdbfZ/Fixenra1t4DFr1qxR+DQAAAAATGbjpmOtVCrllFNOyTPPPJMVK1YMnP/GN76RlpaW7Lvvvnn00Ufzt3/7t+nt7c0999yTqVOn5utf/3re/e53D+pAS5ITTzwx++23Xz73uc9t8V461gAAoDY2neZZXF/M9MunJ0nWLFyT5sbmgWvNU5q3eC0AjIVKOtYaxqim7Xr/+9+f++67LytXrhx0fsP0ziSZPXt2Dj300Oy777658cYbM2/evG3er1QqpVDYepv51KlTM3Xq1JEpHAAAGLZtBWbNjc3CNAAmnHEx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OFibMWNGHnnkkS3Or1y5Mi960YtGpCgAAAAAGO8qDtbe97735YMf/GD+4z/+I4VCIU8++WT+5V/+JQsXLszZZ589GjUCAAAAwLjTUOkLLrjggnR0dOTYY4/N888/n7lz52bq1KlZuHBh3v/+949GjQAAAAAw7hRKpVKpmhc+99xz+cUvfpH+/v4ceOCBaWlpGenaxkxnZ2fa2trS0dGR1tbWWpcDAAAAQI1UkhNVPBV0gyeffDJPP/10DjrooLS0tKTKfA4AAAAAJqSKg7Wnn346r3nNa3LAAQfkT//0T7Nq1aokyXvf+96cf/75I14gAAAAAIxHFQdr5513XhobG/P4449n1113HTj/1re+NTfddNOIFgcAAAAA41XFmxfccsstufnmm7PPPvsMOr///vvnscceG7HCAAAAAGA8q7hjrVgsDupU2+C3v/1tpk6dOiJFAQAAAMB4V3GwNnfu3Hz1q18deF4oFNLf359PfepTOfbYY0e0OAAAAAAYryqeCvqpT30qxxxzTO6+++709PTkggsuyIMPPpjf/e53ueOOO0ajRgAAAAAYdyruWDvwwANz33335VWvelVOOOGEFIvFzJs3Lz//+c/zR3/0R6NRIwAAAACMO4VSqVSqdRG11tnZmba2tnR0dKS1tbXW5QAAAABQI5XkRBVPBU2SZ555Jl/60pfyy1/+MoVCIS95yUvy7ne/O3vssUdVBQMAAADARFPxVNDbb789++23Xz7zmc/kmWeeye9+97t85jOfyX777Zfbb799NGoEAAAAgHGn4qmgs2fPzhFHHJFly5alvr4+SdLX15ezzz47d9xxRx544IFRKXQ0mQoKAAAAQFJZTlRxx9p///d/5/zzzx8I1ZKkvr4+CxYsyH//939XXi0AAAAATEAVB2t/8id/kl/+8pdbnP/lL3+Zl73sZSNREwAAAACMexVvXvCBD3wgH/zgB/PII4/k8MMPT5Lceeed+exnP5tLL700991338DYgw8+eOQqBQAAAIBxpOI11urqhm5yKxQKKZVKKRQK6evr26Hixoo11gAAAABIKsuJKu5Ye/TRR6suDAAAAAAmi4qDtX333Xc06gAAAACACaXiYO2rX/3qkNf/4i/+oupiAAAAAGCiqHiNtd13333Q8/Xr1+e5557LlClTsuuuu+Z3v/vdsO+1ePHiXHvttfmv//qvNDU15Ygjjshll12WP/7jPx4YUyqVsmjRonz+85/PM888k8MOOyyf/exn89KXvnRgzLp167Jw4cL867/+a7q7u/Oa17wmS5cuzT777DOsOqyxBgAAAEBSWU409E4EW/HMM88MenR1deWhhx7KkUcemX/913+t6F6333575s+fnzvvvDO33nprent7c+KJJ6ZYLA6M+eQnP5klS5bkyiuvzF133ZX29vaccMIJefbZZwfGnHvuuVm+fHmuueaarFy5Ml1dXTn55JMnzOYJAADA6Cr2FFNYVEhhUSHFnuL2XzBG9wJgYqu4Y21b7r777rzjHe/If/3Xf1V9j6eeeirTpk3L7bffnrlz56ZUKmXmzJk599xz86EPfShJuTtt+vTpueyyy/K+970vHR0d2XvvvfO1r30tb33rW5MkTz75ZGbNmpXvfve7Oemkk7b7vjrWAABgciv2FNOyuCVJ0nVhV5qnNI+LewEw/oxqx9q21NfX58knn9yhe3R0dCRJ9thjjyTlHUhXr16dE088cWDM1KlTc/TRR+cnP/lJkuSee+7J+vXrB42ZOXNmZs+ePTBmc+vWrUtnZ+egBwAAAABUouLNC7797W8Pel4qlbJq1apceeWVmTNnTtWFlEqlLFiwIEceeWRmz56dJFm9enWSZPr06YPGTp8+PY899tjAmClTpmyx9tv06dMHXr+5xYsXZ9GiRVXXCgAAjH+bTtMsrt/6cZJhdZyN5L0AmDwqDtbe9KY3DXpeKBSy995757jjjss//MM/VF3I+9///tx3331ZuXLlFtcKhcKg56VSaYtzmxtqzIUXXpgFCxYMPO/s7MysWbOqqBoAABivNkzX3Nz0ywf/i/vSRdtfHWck7wXA5FFxsNbf3z/iRZxzzjn59re/nR//+MeDdvJsb29PUu5KmzFjxsD5tWvXDnSxtbe3p6enJ88888ygrrW1a9fmiCOO2Or7TZ06NVOnTh3xzwEAAADAzqPiYG1brr322lx88cW57777hv2aUqmUc845J8uXL89tt92W/fbbb9D1/fbbL+3t7bn11lvz8pe/PEnS09OT22+/PZdddlmS5BWveEUaGxtz66235rTTTkuSrFq1Kg888EA++clPjtCnAwAAJpquC7sGjovriwPdZWsWrklzY2VTNkfyXgBMHhUFa1/4whdyyy23pLGxMR/4wAdy+OGH54c//GHOP//8PPTQQ3nnO99Z0ZvPnz8/X//613P99ddnt912G1gTra2tLU1NTSkUCjn33HNzySWXZP/998/++++fSy65JLvuumve/va3D4x9z3vek/PPPz977rln9thjjyxcuDAHHXRQjj/++IrqAQAAJo9trXfW3Nhc8VpoI3kvACaPYQdrl19+eT7ykY/k4IMPzi9/+ctcf/31+ehHP5olS5bknHPOyfz587PXXntV9ObLli1LkhxzzDGDzn/5y1/OGWeckSS54IIL0t3dnbPPPjvPPPNMDjvssNxyyy3ZbbfdBsZfccUVaWhoyGmnnZbu7u685jWvydVXX536+vqK6gEAAACA4SqUSqVhra75kpe8JP/3//7f/OVf/mVuu+22HHfccTnuuOPyzW9+My94wQtGuczR1dnZmba2tnR0dKS1tbXW5QAAACOs2FMc2ICg68KuHeoyG8l7ATD+VJITDbtj7bHHHhuYWnnMMceksbExn/jEJyZ8qAYAABOFQKd6xZ7ioOMd+e6apzTb/ROAJEndcAc+//zz2WWXXQaeT5kyJXvvvfeoFAUAAAAA411Fmxd88YtfTEtL+d+Q9fb25uqrr95iXbUPfOADI1cdAAAAAIxTww7WXvjCF+YLX/jCwPP29vZ87WtfGzSmUCgI1gAAYAQNmsK4fuvHybZ3rdyZre1aO3D81HNPbfU4Saa1TBuzmgCYXIa9ecFkZvMCAADGq8KiwrDGWfNrS747AKpRSU407DXWAAAAAICNKlpjDQAAGFtdF3YNHBfXFzP98ulJkjUL16S50fTPoaw5f83A8VPPPZXZy2YnSR4464HsvauN2ADYcYI1AAAYx7a1dlpzY7N11bZjW2un7b3r3tZVA2BEmAoKAAAAAFUQrAEAAABAFaqaCtrf359HHnkka9euTX9//6Brc+fOHZHCAACAwZqnNNvBskrTWqb57gAYcRUHa3feeWfe/va357HHHkupNPi/mAqFQvr6+kasOAAAAAAYryoO1s4888wceuihufHGGzNjxowUCoXRqAsAAAAAxrWKg7WHH3443/zmN/PiF794NOoBAAAAgAmh4s0LDjvssDzyyCOjUQsAAAAATBgVd6ydc845Of/887N69eocdNBBaWxsHHT94IMPHrHiAAAmqmJPMS2LW5IkXRd2pXlKc40rAgBgpFUcrL35zW9OkvzlX/7lwLlCoZBSqWTzAgAAAAB2GhUHa48++uho1AEAAAAAE0rFwdq+++47GnUAAEx4xZ7ixuP1Wz9OYlooAMAkUXGwtsEvfvGLPP744+np6Rl0/o1vfOMOFwUAMBFtWFNtc9Mvnz7oeemi0liUAwDAKKs4WPuf//mfnHrqqbn//vsH1lZLyuusJbHGGgAAAAA7hYqDtQ9+8IPZb7/98v3vfz8vetGL8p//+Z95+umnc/755+fyyy8fjRoBACaErgu7Bo6L64sDnWprFq5Jc6PpnwAAk03FwdpPf/rT/PCHP8zee++durq61NXV5cgjj8zixYvzgQ98ID//+c9Ho04AgHFvW2unNTc2W1cNAGASqqv0BX19fWlpKa8fstdee+XJJ59MUt7U4KGHHhrZ6gAAAABgnKq4Y2327Nm577778qIXvSiHHXZYPvnJT2bKlCn5/Oc/nxe96EWjUSMAAAAAjDsVB2t/8zd/k2KxvGX8xz/+8Zx88sk56qijsueee+Yb3/jGiBcIADARNU9ptvsnAMAkVyht2NZzB/zud7/L7rvvPrAz6ETT2dmZtra2dHR0pLW1tdblAAAAAFAjleREFXesbc0ee+wxErcBAAAAgAljWMHavHnzcvXVV6e1tTXz5s0bcuy11147IoUBAAAAwHg2rGCtra1tYJpnW1vbqBYEAAAAABPBiKyxNtFZYw0AAACApLKcqG6MagIAAACASWVYU0Ff/vKXD3vHz5/97Gc7VBAAAAAATATDCtbe9KY3DRw///zzWbp0aQ488MC8+tWvTpLceeedefDBB3P22WePSpEAAAAAMN4MK1i76KKLBo7f+9735gMf+ED+/u//fosxTzzxxMhWBwAAAADjVMWbF7S1teXuu+/O/vvvP+j8ww8/nEMPPTQdHR0jWuBYsHkBAAAAAMkob17Q1NSUlStXbnF+5cqV2WWXXSq9HQAAAABMSMOaCrqpc889N2eddVbuueeeHH744UnKa6z90z/9Uz72sY+NeIEAAAAAMB5VHKx9+MMfzote9KL84z/+Y77+9a8nSV7ykpfk6quvzmmnnTbiBQIAANtW7CmmZXFLkqTrwq40T2mucUUAsPOoOFhLktNOO02IBgAAAMBOrapgLUl6enqydu3a9Pf3Dzr/whe+cIeLAgAAAIDxruJg7eGHH85f/uVf5ic/+cmg86VSKYVCIX19fSNWHAAAsKViT3Hj8fqtHycxLRQARlnFwdoZZ5yRhoaGfOc738mMGTNSKBRGoy4AAGAbNqyptrnpl08f9Lx0UWksygGAnVbFwdq9996be+65J//n//yf0agHAAAAACaEioO1Aw88ML/97W9HoxYAAGAYui7sGjguri8OdKqtWbgmzY2mfwLAWKmr9AWXXXZZLrjggtx22215+umn09nZOegBAACMruYpzRsfmwRpzY3Ng64BAKOr4o61448/Pknymte8ZtB5mxcAAAAAsDOpOFj70Y9+NBp1AAAAAMCEUnGwdvTRR49GHQAAQBWapzTb/RMAamTYwdp99903rHEHH3xw1cUAAAAAwEQx7GDtZS97WQqFQkqlbf/bMGusAQAAALCzGHaw9uijj45mHQAAjJJiTzEti1uSJF0XdtktEgBghAw7WNt3331Hsw4AAAAAmFDqal0AAAAAAExEFe8KCgDA+FfsKW48Xr/14ySmhQIA7ADBGgDAJLRhTbXNTb98+qDnpYu2vTEVAABDMxUUAAAAAKqgYw0AYBLqurBr4Li4vjjQqbZm4Zo0N5r+CQAwEiruWFuzZk3e+c53ZubMmWloaEh9ff2gBwAAtdc8pXnjY5MgrbmxedA1AACqV3HH2hlnnJHHH388f/u3f5sZM2akUCiMRl0AAAAAMK5VHKytXLkyK1asyMte9rJRKAcAAAAAJoaKg7VZs2alVLJ7FADARNE8pdnunwAAo6DiNdY+/elP58Mf/nB+9atfjUI5AAAAADAxDKtjbffddx+0llqxWMwf/dEfZdddd01jY+Ogsb/73e9GtkIAAAAAGIeGFax9+tOfHuUyAAAAAGBiGVaw9q53vWtYN+vu7t6hYgAAAABgoqh4jbX58+dv9XyxWMzrXve6HS4IAAAAACaCioO1W265JX/zN38z6FyxWMxrX/va9PX1jVhhAAAAADCeDWsq6KZuueWWHHnkkdlzzz1z3nnn5dlnn81JJ52UhoaGfO973xuNGgEAAABg3Kk4WNtvv/1y880355hjjkldXV2uueaaTJ06NTfeeGOam5tHo0YAAAAAGHcqDtaSZPbs2fnOd76T448/Pocddli+853vpKmpaaRrAwAAAIBxa1jB2stf/vIUCoUtzk+dOjVPPvlk5syZM3DuZz/72chVBwAAAADj1LCCtTe96U2jXAYAAAAATCyFUqlUqnURtdbZ2Zm2trZ0dHSktbW11uUAAAAAUCOV5ER1Y1QTAAAAAEwqFW9e0NfXlyuuuCL/9m//lscffzw9PT2Drv/ud78bseIAAAAAYLyquGNt0aJFWbJkSU477bR0dHRkwYIFmTdvXurq6nLxxRePQokAABNTsaeYwqJCCosKKfYUa10OAAAjrOJg7V/+5V/yhS98IQsXLkxDQ0NOP/30fPGLX8zHPvax3HnnnaNRIwAAAACMOxUHa6tXr85BBx2UJGlpaUlHR0eS5OSTT86NN944stUBAAAAwDhVcbC2zz77ZNWqVUmSF7/4xbnllluSJHfddVemTp06stUBAEwwxZ7ixsf6jdM/i+uLg64BADDxVbx5wamnnpof/OAHOeyww/LBD34wp59+er70pS/l8ccfz3nnnTcaNQIATBgti1u2en765dMHPS9dVBqLcgAAGEUVB2uXXnrpwPFb3vKWzJo1K3fccUde/OIX541vfOOIFgcAAAAA41WhVCqNyL8uXbNmTT73uc/lYx/72Ejcbkx1dnamra0tHR0daW1trXU5AMAEtuk0z+L64kCn2pqFa9Lc2DxwrXlK8xavBQCg9irJiSpeY21bVq9enUWLFo3U7QAAJqTmKc0bH5sGaY3Ng64BADDxjViwBgAAAAA7E8EaAAAAAFSh4s0LAAAYnuYpzXb/BACYxIYdrC1YsGDI60899dQOFwMAAAAAE8Wwg7Wf//zn2x0zd+7cHSoGAAAAACaKYQdrP/rRj0azDgAAAACYUGxeAAAAAABVGFawdumll6ZYLA7rhv/xH/+RG2+8cYeKAgAAAIDxbljB2i9+8Yvsu+++Oeuss/K9731v0EYFvb29ue+++7J06dIcccQRedvb3pbW1tZRKxgAAAAAxoNhrbH21a9+Nffdd18++9nP5s///M/T0dGR+vr6TJ06Nc8991yS5OUvf3n++q//Ou9617syderUUS0aAAAAAGqtUCqVSpW8oFQq5b777suvfvWrdHd3Z6+99srLXvay7LXXXqNV46jr7OxMW1tbOjo6dNsBAAAA7MQqyYmGvSvoBoVCIYccckgOOeSQqgsEAAAAgInOrqAAAAAAUAXBGgAAAABUQbAGAAAAAFUQrAEAAABAFaoO1h555JHcfPPN6e7uTlLeLRQAAAAAdhYVB2tPP/10jj/++BxwwAH50z/906xatSpJ8t73vjfnn3/+iBcIAJNRsaeYwqJCCosKKfYUa10OAABQhYqDtfPOOy8NDQ15/PHHs+uuuw6cf+tb35qbbrppRIsDAAAAgPGqodIX3HLLLbn55puzzz77DDq///7757HHHhuxwgAAAABgPKs4WCsWi4M61Tb47W9/m6lTp45IUQAwGW065bO4fuvHSdI8pXnMagIAAKpXcbA2d+7cfPWrX83f//3fJ0kKhUL6+/vzqU99Kscee+yIFwgAk0XL4patnp9++fRBz0sX2RAIAAAmgoqDtU996lM55phjcvfdd6enpycXXHBBHnzwwfzud7/LHXfcMRo1AgAAAMC4U3GwduCBB+a+++7LsmXLUl9fn2KxmHnz5mX+/PmZMWPGaNQIAJNC14VdA8fF9cWBTrU1C9ekudH0TwAAmGgqDtaSpL29PYsWLRrpWgBgUtvW2mnNjc3WVQMAgAmortIXfPnLX86///u/b3H+3//93/OVr3xlRIoCAAAAgPGu4mDt0ksvzV577bXF+WnTpuWSSy4ZkaIAAAAAYLyreCroY489lv3222+L8/vuu28ef/zxESkKACa75inNdv8EAIAJruKOtWnTpuW+++7b4vz/+3//L3vuueeIFAUAAAAA413Fwdrb3va2fOADH8iPfvSj9PX1pa+vLz/84Q/zwQ9+MG9729tGo0YAAAAAGHcqngr68Y9/PI899lhe85rXpKGh/PL+/v78xV/8hTXWAIAJo9hTTMviliRJ14VddmYFAKBiFXesTZkyJd/4xjfyX//1X/mXf/mXXHvttfnv//7v/NM//VOmTJlS0b1+/OMf5w1veENmzpyZQqGQ6667btD1M844I4VCYdDj8MMPHzRm3bp1Oeecc7LXXnulubk5b3zjG/PrX/+60o8FAAAAABWpuGNtgwMOOCAHHHDADr15sVjMIYcckne/+91585vfvNUxr33ta/PlL3954Pnm4d25556bG264Iddcc0323HPPnH/++Tn55JNzzz33pL6+fofqAwAAAIBtGVawtmDBgvz93/99mpubs2DBgiHHLlmyZNhv/rrXvS6ve93rhhwzderUtLe3b/VaR0dHvvSlL+VrX/tajj/++CTJP//zP2fWrFn5/ve/n5NOOmnYtQAAk1+xp7jxeP3Wj5OYFgoAwLAMK1j7+c9/nvXr1ydJfvazn6VQKGx13LbO74jbbrst06ZNywte8IIcffTR+cQnPpFp06YlSe65556sX78+J5544sD4mTNnZvbs2fnJT36yzWBt3bp1Wbdu3cDzzs7OEa8bABh/Nqyptrnpl08f9Lx0UWksygEAYIIbVrD2ox/9aOD4tttuG61atvC6170uf/Znf5Z99903jz76aP72b/82xx13XO65555MnTo1q1evzpQpU7L77rsPet306dOzevXqbd538eLFWbRo0WiXDwAAAMAkVtEaa729vdlll11y7733Zvbs2aNV04C3vvWtA8ezZ8/OoYcemn333Tc33nhj5s2bt83XlUqlIbvnLrzwwkFTWjs7OzNr1qyRKRoAGLe6LuwaOC6uLw50qq1ZuCbNjaZ/AgBQmYqCtYaGhuy7777p6+sbrXqGNGPGjOy77755+OGHkyTt7e3p6enJM888M6hrbe3atTniiCO2eZ+pU6dm6tSpo14vADC+bGvttObGZuuqAQBQsbpKX/A3f/M3ufDCC/O73/1uNOoZ0tNPP50nnngiM2bMSJK84hWvSGNjY2699daBMatWrcoDDzwwZLAGAAAAADuqoo61JPnMZz6TRx55JDNnzsy+++6b5ubB/3b3Zz/72bDv1dXVlUceeWTg+aOPPpp77703e+yxR/bYY49cfPHFefOb35wZM2bkV7/6VT7ykY9kr732yqmnnpokaWtry3ve856cf/752XPPPbPHHntk4cKFOeiggwZ2CQUAAACA0VBxsHbKKaeM2O6fd999d4499tiB5xvWPXvXu96VZcuW5f77789Xv/rV/P73v8+MGTNy7LHH5hvf+EZ22223gddcccUVaWhoyGmnnZbu7u685jWvydVXX536+voRqREAmJyapzTb/RMAgB1SKJVKO/3/ouzs7ExbW1s6OjrS2tpa63IAAAAAqJFKcqJhr7H23HPPZf78+fmDP/iDTJs2LW9/+9vz29/+doeLBQAAAICJaNjB2kUXXZSrr746r3/96/O2t70tt956a84666zRrA0AAAAAxq1hr7F27bXX5ktf+lLe9ra3JUne8Y53ZM6cOenr67OeGQAAAAA7nWF3rD3xxBM56qijBp6/6lWvSkNDQ5588slRKQwAAAAAxrNhB2t9fX2ZMmXKoHMNDQ3p7e0d8aIAAAAAYLwb9lTQUqmUM844I1On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u87OYGf6Pd9ep9oGNi8AAAAAgCoI1gAAAACgCoI1mACmTp2aiy66KFOnTq11KTCq/K6zM/B7zs7C7zo7C7/r7Az8nm+bzQsAAAAAoAo61gAAAACgCoI1AAAAAKiCYA0AAAAAqiBYAwAAAIAqCNZgjPz4xz/OG97whsycOTOFQiHXXXfdoOulUikXX3xxZs6cmaamphxzzDF58MEHB41Zt25dzjnnnOy1115pbm7OG9/4xvz6178eNOaZZ57JO9/5zrS1taWtrS3vfOc78/vf/36UPx1stL3f9TPOOCOFQmHQ4/DDDx80xu86493ixYvzyle+MrvttlumTZuWN73pTXnooYcGjfF3nYluOL/n/qYzGSxbtiwHH3xwWltb09ramle/+tX53ve+N3Dd33Mmg+39nvt7Xj3BGoyRYrGYQw45JFdeeeVWr3/yk5/MkiVLcuWVV+auu+5Ke3t7TjjhhDz77LMDY84999wsX74811xzTVauXJmurq6cfPLJ6evrGxjz9re/Pffee29uuumm3HTTTbn33nvzzne+c9Q/H2ywvd/1JHnta1+bVatWDTy++93vDrrud53x7vbbb8/8+fNz55135tZbb01vb29OPPHEFIvFgTH+rjPRDef3PPE3nYlvn332yaWXXpq77747d999d4477riccsopA+GZv+dMBtv7PU/8Pa9aCRhzSUrLly8feN7f319qb28vXXrppQPnnn/++VJbW1vpqquuKpVKpdLvf//7UmNjY+maa64ZGPOb3/ymVFdXV7rppptKpVKp9Itf/KKUpHTnnXcOjPnpT39aSlL6r//6r1H+VLClzX/XS6VS6V3velfplFNO2eZr/K4zEa1du7aUpHT77beXSiV/15mcNv89L5X8TWfy2n333Utf/OIX/T1nUtvwe14q+Xu+I3SswTjw6KOPZvXq1TnxxBMHzk2dOjVHH310fvKTnyRJ7rnnnqxfv37QmJkzZ2b27NkDY37605+mra0thx122MCYww8/PG1tbQNjYDy47bbbMm3atBxwwAH5q7/6q6xdu3bgmt91JqKOjo4kyR577JHE33Ump81/zzfwN53JpK+vL9dcc02KxWJe/epX///bu/egqMo3DuDfVUE3F1dFbgUuKEmsmiNgCYbXAlp1VMjRwoIsjRxvZWYyammWzpi3qXFkmhXTbMIKmlRmCBC5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\n",
      "text/plain": [
       "<Figure size 1500x1000 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "    \n",
    "plot_scatter_chart(df7,\"Hebbal\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5403db8",
   "metadata": {},
   "source": [
    "We should also remove properties where for same location, the price of (for example) 3 bedroom apartment is less than 2 bedroom apartment (with same square ft area). What we will do is for a given location, we will build a dictionary of stats per bhk, i.e.\n",
    "\n",
    "{\n",
    "    '1' : {\n",
    "        'mean': 4000,\n",
    "        'std: 2000,\n",
    "        'count': 34\n",
    "    },\n",
    "    '2' : {\n",
    "        'mean': 4300,\n",
    "        'std: 2300,\n",
    "        'count': 22\n",
    "    },    \n",
    "}\n",
    "Now we can remove those 2 BHK apartments whose price_per_sqft is less than mean price_per_sqft of 1 BHK apartment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "8aada0b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7329, 7)"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def remove_bhk_outliers(df):\n",
    "    exclude_indices = np.array([])\n",
    "    for location, location_df in df.groupby('location'):\n",
    "        bhk_stats = {}\n",
    "        for bhk, bhk_df in location_df.groupby('bhk'):\n",
    "            bhk_stats[bhk] = {\n",
    "                'mean': np.mean(bhk_df.price_per_sqft),\n",
    "                'std': np.std(bhk_df.price_per_sqft),\n",
    "                'count': bhk_df.shape[0]\n",
    "            }\n",
    "        for bhk, bhk_df in location_df.groupby('bhk'):\n",
    "            stats = bhk_stats.get(bhk-1)\n",
    "            if stats and stats['count']>5:\n",
    "                exclude_indices = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)\n",
    "    return df.drop(exclude_indices,axis='index')\n",
    "df8 = remove_bhk_outliers(df7)\n",
    "# df8 = df7.copy()\n",
    "df8.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "f3743231",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABNYAAANVCAYAAAC09nNHAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQGoP6dpAAB0x0lEQVR4nOzdeXxddZ0//tfNVkvahM1utlNRYRRbFMERaKnsywgU6gwo44LLfOm0oFA6KqACLmxiq/60xYUB18FxaEFGRUAEKcKILLLIKDpsSheVmpAQmja5vz8yBEK35DR7ns/H4z7uPed8zsn7tId6feWzlMrlcjkAAAAAQI9UDHQBAAAAADAUCdYAAAAAoADBGgAAAAAUIFgDAAAAgAIEawAAAABQgGANAAAAAAoQrAEAAABAAYI1AAAAAChAsAYAAAAABQjWAAB6wRVXXJFSqdT5qqqqysSJE/O2t70tDz/8cOHrvvzlL89JJ53UK+c++uijKZVKueKKK7Z43nPtSqVSrrzyyo2On3vuuSmVSvnzn/9cqC4AgOGiaqALAAAYTi6//PK8+tWvzrPPPpvbbrstn/70p/PTn/40//M//5Mddtihx9dbvnx56urqCtXy4nMnTpyY22+/Pa985Su7fY2zzz47b33rW1NdXV2oBgCA4UyPNQCAXjRt2rTss88+OeCAA3L22WfnIx/5SNasWZOrr7660PX23HPPHgVhWzp31KhR2WefffLSl760W+cfeeSR+d///d9ceumlhX7+QHrmmWcGugQAYAQQrAEA9KG99947SbJ69erOfc8++2zOOOOMvP71r099fX123HHH7Lvvvrnmmms2Ov/Fwzm35dzuDgV9zkEHHZTDDz88n/zkJ/P0009vse0NN9yQ2bNnZ/LkyXnJS16SV73qVTn55JM3OVz0mmuuyR577JFRo0blFa94RT7/+c93Di99oS996UuZNWtWxo0bl9ra2kyfPj0XX3xx1q9f36XdAQcckGnTpuVnP/tZ9ttvv2y33XZ573vf2617BADYFoaCAgD0oUceeSRJsttuu3XuW7duXZ566qksXLgwL3vZy9La2pobb7wxc+bMyeWXX553vetdm73etpxbxEUXXZQ999wzn/nMZ/KJT3xis+1+//vfZ99998373//+1NfX59FHH82iRYsyc+bM3H///Z1DSa+77rrMmTMns2bNyne/+91s2LAhl1xySZfg8YXXPPHEE7PLLrukpqYmv/rVr/LpT386//M//5N/+7d/69J25cqVecc73pEPfehDOf/881NR4ffHAEDfE6wBAPSitra2bNiwoXOOtU996lOZNWtWjjnmmM429fX1ufzyy7ucc/DBB2ft2rX53Oc+t8VwbFvOLeJ1r3tdTjzxxCxatCjz5s3LhAkTNtlu7ty5nZ/L5XL222+/HHDAAZk6dWp+9KMfdd7/xz/+8bzsZS/Lj3/849TU1CRJjjjiiLz85S/f6JqLFi3q/Nze3p79998/O+20U97znvfks5/9bJc565566ql873vfy0EHHdQbtw0A0C1+lQcA0Iv22WefVFdXZ+zYsTniiCOyww475JprrklVVdffZ37ve9/LjBkzMmbMmFRVVaW6ujqXXXZZHnrooa3+jG05t4hPfepTWb9+fc4777zNtlmzZk3mzp2bKVOmdNY0derUJOmsq7m5Ob/85S9z7LHHdoZqSTJmzJgcffTRG13znnvuyTHHHJOddtoplZWVqa6uzrve9a60tbXlt7/9bZe2O+ywg1ANAOh3gjUAgF70jW98I3feeWduuummnHzyyXnooYfy9re/vUubZcuW5fjjj8/LXvayfOtb38rtt9+eO++8M+9973vz7LPPbvH623JuUS9/+cszb968fO1rX8vDDz+80fH29vYcdthhWbZsWT70oQ/lJz/5SX7xi1/kjjvuSJK0tLQkSdauXZtyuZzx48dvdI0X73v88cez//77549//GM+//nP59Zbb82dd96ZL33pS12u+ZyJEyf2yr0CAPSEoaAAAL3oNa95TeeCBQceeGDa2tryta99Lf/5n/+Zf/iHf0iSfOtb38ouu+yS7373u10m7F+3bt1Wr78t526Lj370o/m3f/u3nHXWWXnta1/b5dgDDzyQX/3qV7niiivy7ne/u3P/7373uy7tdthhh5RKpU3Op7Zq1aou21dffXWam5uzbNmyzp5vSXLvvfdusr4XL3wAANAf9FgDAOhDF198cXbYYYd8/OMfT3t7e5KOEKimpqZLGLRq1apNruz5Ytty7rbYaaed8uEPfzj/+Z//mV/84hcb1ZQko0aN6rL/y1/+cpft2tra7L333rn66qvT2traub+pqSn/9V//tdVrlsvlfPWrX932mwEA6CWCNQCAPrTDDjvkzDPPzEMPPZTvfOc7SZKjjjoqv/nNbzJv3rzcdNNN+frXv56ZM2d2azjjtpy7rU477bRMmjQpP/rRj7rsf/WrX51XvvKV+chHPpJ///d/z49//OOccsop+f73v7/RNT7xiU/kj3/8Yw4//PBcffXVueqqq3LIIYdkzJgxXcLCQw89NDU1NXn729+eH/3oR1m+fHkOP/zwrF27ts/vEwCguwRrAAB97NRTT83f/M3f5BOf+ETa2trynve8JxdeeGF+9KMf5e///u9z0UUX5SMf+UhOPPHETZ7/wsBpW87dVtttt13OPffcjfZXV1fn2muvzW677ZaTTz45b3/727NmzZrceOONG7U94ogjctVVV+Uvf/lLTjjhhCxYsCDHHXdcZs+ene23376z3atf/epcddVVWbt2bebMmZNTTz01r3/96/OFL3yh1+4HAGBblcrlcnmgiwAAYNN23HHHvPe9780ll1zSr+f2p/Xr1+f1r399Xvayl+X6668f6HIAALrN4gUAAIPQfffdlx/+8IdZu3Zt9t133347tz+8733vy6GHHpqJEydm1apVufTSS/PQQw/l85///ECXBgDQI4I1AIBB6IMf/GD+53/+JwsXLsycOXP67dz+8PTTT2fhwoX505/+lOrq6rzhDW/ID3/4wxxyyCEDXRoAQI8YCgoAAAAABVi8AAAAAAAKEKwBAAAAQAGCNQAAAAAowOIFSdrb2/Pkk09m7NixKZVKA10OAAAAAAOkXC7n6aefzqRJk1JRseU+aYK1JE8++WSmTJky0GUAAAAAMEg88cQTmTx58hbbCNaSjB07NknHH1hdXd0AVwMAAADAQGlsbMyUKVM686ItEawlncM/6+rqBGsAAAAAdGu6MIsXAAAAAEABgjUAAAAAKECwBgAAAAAFmGOtm8rlcjZs2JC2traBLmXYqqysTFVVVbfGMAMAAAAMNMFaN7S2tmblypV55plnBrqUYW+77bbLxIkTU1NTM9ClAAAAAGyRYG0r2tvb88gjj6SysjKTJk1KTU2NHlV9oFwup7W1NX/605/yyCOPZNddd01FhZHKAAAAwOAlWNuK1tbWtLe3Z8qUKdluu+0GupxhbfTo0amurs5jjz2W1tbWvOQlLxnokgAAAAA2S5egbtJ7qn/4cwYAAACGCikGAAAAABQgWAMAAACAAgRrAAAAAFCAYK0ftbQkq1d3vPe1Cy64IG984xszduzYjBs3Lscee2x+85vfbPGcK664IqVSqfM1ZsyY7LXXXlm2bFmXdgcccEBOO+20TZ6//fbbb3Y7SR566KFMnjw5c+bMybp164reHgAAAMCAE6z1gxUrkjlzkjFjkgkTOt7nzEluu63vfuYtt9yS+fPn54477sgNN9yQDRs25LDDDktzc/MWz6urq8vKlSuzcuXK3HPPPTn88MNz/PHHbzWU644777wz+++/fw4//PB873vfy6hRo7b5mgAAAAADRbDWx5YuTWbNSq69Nmlv79jX3t6xvf/+yaWX9s3Pve6663LSSSflta99bV73utfl8ssvz+OPP5677rpri+eVSqVMmDAhEyZMyK677ppPfepTqaioyH333bdN9dx000056KCD8p73vCeXXXZZKisrt+l6AAAAAANNsNaHVqxI5s9PyuVkw4auxzZs6Ng/b17f9lx7TkNDQ5Jkxx137PY5bW1t+frXv54kecMb3lD4Zy9fvjxvectbcvbZZ+czn/lM4esAAAAADCZVA13AcLZoUVJZuXGo9kKVlcnixcmMGX1XR7lczoIFCzJz5sxMmzZti20bGhoyZsyYJElLS0uqq6vzla98Ja985Su7tFuyZEm+9rWvddm3YcOGvOQlL+myr6mpKf/4j/+Ys846Kx/5yEd64W4AAAAABgfBWh9paUmuueb54Z+bs2FDsnx5R/vRo/umllNOOSX33XdfVqxYsdW2Y8eOzd13350keeaZZ3LjjTfm5JNPzk477ZSjjz66s90//dM/5eyzz+5y7rJly3L++ed32Td69OjMnDkzX/3qV/P2t789r3nNa3rhjgAAAAAGnmCtjzQ2bj1Ue057e0f7vgjWTj311Hz/+9/Pz372s0yePHmr7SsqKvKqV72qc3uPPfbI9ddfn4suuqhLsFZfX9+lXZKMGzduo+tVVlbm6quvzlvf+tYceOCBuemmm7L77rtvwx0BAAAADA7mWOsjdXVJRTf/dCsqOtr3pnK5nFNOOSXLli3LTTfdlF122aXwtSorK9PS0lL4/FGjRmXZsmX5u7/7uxx44IF54IEHCl8LAAAAYLAQrPWR0aOT2bOTqq30CayqSo47rvd7q82fPz/f+ta38p3vfCdjx47NqlWrsmrVqq0GZOVyubPtI488kq985Sv58Y9/nNmz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lStXdr5++MMfdrnGaaedluXLl+fKK6/MihUr0tTUlKOOOiptbW39fTsAAAAAjCBVA/nDjz766C7bn/70p7N06dLccccdee1rX5skGTVqVCZMmLDJ8xsaGnLZZZflm9/8Zg455JAkybe+9a1MmTIlN954Yw4//PC+vQEAAACAbfDCIZ/N6zf9OUlqa2r7rSa6b0CDtRdqa2vL9773vTQ3N2ffffft3H/zzTdn3Lhx2X777fPmN785n/70pzNu3LgkyV133ZX169fnsMMO62w/adKkTJs2LT//+c83G6ytW7cu69at69xubGzso7sCAAAA2LwxF4zZ5P7xl4zvsl0+p9wf5dBDA754wf33358xY8Zk1KhRmTt3bpYvX57dd989SXLkkUfm29/+dm666aZ89rOfzZ133pmDDjqoMxRbtWpVampqssMOO3S55vjx47Nq1arN/swLLrgg9fX1na8pU6b03Q0CAAAAMCwNeI+1v/3bv829996bv/71r7nqqqvy7ne/O7fcckt23333nHDCCZ3tpk2blr333jtTp07ND37wg8yZM2ez1yyXyymVSps9fuaZZ2bBggWd242NjcI1AAAAoN81ndnU+bl5fXNnT7XVC1enttrwz8FuwIO1mpqavOpVr0qS7L333rnzzjvz+c9/Pl/+8pc3ajtx4sRMnTo1Dz/8cJJkwoQJaW1tzdq1a7v0WluzZk3222+/zf7MUaNGZdSoUb18JwAAAAA9s7m502qra82rNgQM+FDQFyuXy13mP3uhv/zlL3niiScyceLEJMlee+2V6urq3HDDDZ1tVq5cmQceeGCLwRoAAAAAbKsB7bF21lln5cgjj8yUKVPy9NNP58orr8zNN9+c6667Lk1NTTn33HPz1re+NRMnTsyjjz6as846KzvvvHOOO+64JEl9fX3e97735YwzzshOO+2UHXfcMQsXLsz06dM7VwkFAAAAgL4woMHa6tWr8853vjMrV65MfX199thjj1x33XU59NBD09LSkvvvvz/f+MY38te//jUTJ07MgQcemO9+97sZO3Zs5zUWL16cqqqqHH/88WlpacnBBx+cK664IpWVlQN4ZwAAAAA9U1tTa/XPIaZULpdH/N9YY2Nj6uvr09DQkLq6uoEuBwAAAIAB0pOcaNDNsQYAAAAAQ4FgDQAAAAAKEKwBAAAAQAGCNQAAAAAoQLAGAAAAAAUI1gAAAACgAMEaAAAAABQgWAMAAACAAgRrAAAAAFCAYA0AAAAAChCsAQAAAEABgjUAAAAYoZpbm1M6r5TSeaU0tzYPdDkjnr+PoUewBgAAAAAFCNYAAAAAoICqgS4AAAAA6D8vHGLYvH7Tn5Oktqa232oayfx9DG2lcrlcHugiBlpjY2Pq6+vT0NCQurq6gS4HAAAA+kzpvFK32pXPGfFxQb/w9zH49CQnMhQUAAAAAAowFBQAAABGkKYzmzo/N69vzvhLxidJVi9cndpqww37m7+PoU2wBgAAACPI5ubqqq2uNY/XAPD3MbQZCgoAAAAABQjWAAAAAKAAQ0EBAABghKqtqbXa5CDi72Po0WMNAAAAAAoQrAEAAABAAYI1AAAAAChAsAYAAAD0SHNrc0rnlVI6r5Tm1uaBLgcGjGANAAAAAAoQrAEAAABAAVUDXQAAAAAw+L1wyGfz+k1/TpLamtp+qwkGmmANAAAA2KoxF4zZ5P7xl4zvsl0+p9wf5cCgYCgoAAAAABSgxxoAAACwVU1nNnV+bl7f3NlTbfXC1amtNvyTkUmwBgAAAGzV5uZOq62uNa8aI5ahoAAAAABQgGANAAAAAAowFBQAAADokdqaWqt/QvRYAwAAAIBCBGsAAAAAUIBgDQAAAAAKEKwBAAAAQAGCNQAAAAAoQLAGAAAAAAUI1gAAAACgAMEaAAAAABQgWAMAAACAAgRrAAAAAFCAYA0AAAAAChCsAQAAAEABgjUAAAAAKECwBgAAAAAFCNYAAAAAoADBGgAAAAAUIFgDAAAAgAIEawAAAABQgGANAAAAAAoQrAEAAABAAYI1AAAAAChAsAYAAAAABQjWAAAAAKAAwRoAAAAAFCBYAwAAAIACBGsAAAAAUIBgDQAAAAAKEKwBAAAAQAGCNQAAAAAoQLAGAAAAAAUI1gAAAACgAMEaAAAAABQgWAMAAACAAgRrAAAAAFCAYA0AAAAAChCsAQAAAEABgjUAAAAAKECwBgAAAAAFCNYAAAAAoADBGgAAAAAUIFgDAAAAgAKqetK4oaEhy5cvz6233ppHH300zzzzTF760pdmzz33zOGHH5799tuvr+oEAAAAgEGlWz3WVq5cmX/+53/OxIkT84lPfCLNzc15/etfn4MPPjiTJ0/OT3/60xx66KHZfffd893vfrevawYAAACAAdetHmuve93r8q53vSu/+MUvMm3atE22aWlpydVXX51FixbliSeeyMKFC3u1UAAAAAAYTErlcrm8tUZ/+tOf8tKXvrTbF+1p+4HW2NiY+vr6NDQ0pK6ubqDLAQAAAGCA9CQn6tZQ0J6GZEMpVAMAAACAInq8KujXv/71/OAHP+jc/tCHPpTtt98+++23Xx577LFeLQ4AAAAABqseB2vnn39+Ro8enSS5/fbb88UvfjEXX3xxdt5555x++um9XiAAAAAADEbdWrzghZ544om86lWvSpJcffXV+Yd/+If8v//3/zJjxowccMABvV0fAAAAAAxKPe6xNmbMmPzlL39Jklx//fU55JBDkiQveclL0tLS0rvVAQAAAMAg1eMea4ceemje//73Z88998xvf/vbvOUtb0mSPPjgg3n5y1/e2/UBAAAAwKDU4x5rX/rSl7LvvvvmT3/6U6666qrstNNOSZK77rorb3/723u9QAAAAAAYjErlcrk80EUMtMbGxtTX16ehoSF1dXUDXQ4AAAAAA6QnOVGPe6wlya233pp3vOMd2W+//fLHP/4xSfLNb34zK1asKHI5AAAAABhyehysXXXVVTn88MMzevTo3H333Vm3bl2S5Omnn87555/f6wUCAAAAwGDU42DtU5/6VC699NJ89atfTXV1def+/fbbL3fffXevFgcAAAAAg1WPg7Xf/OY3mTVr1kb76+rq8te//rU3agIAAACAQa/HwdrEiRPzu9/9bqP9K1asyCte8YpeKQoAAAAABrseB2snn3xyPvjBD+a///u/UyqV8uSTT+bb3/52Fi5cmHnz5vVFjQAAAAAw6FT19IQPfehDaWhoyIEHHphnn302s2bNyqhRo7Jw4cKccsopfVEjAAAAAAw6pXK5XC5y4jPPPJNf//rXaW9vz+67754xY8b0dm39prGxMfX19WloaEhdXd1AlwMAAADAAOlJTtTjoaDPefLJJ/OXv/wl06dPz5gxY1IwnwMAAACAIanHwdpf/vKXHHzwwdltt93y93//91m5cmWS5P3vf3/OOOOMXi8QAAAAAAajHgdrp59+eqqrq/P4449nu+2269x/wgkn5LrrruvV4gAAAABgsOrx4gXXX399fvzjH2fy5Mld9u+666557LHHeq0wAAAAABjMetxjrbm5uUtPtef8+c9/zqhRo3qlKAAAAAAY7HocrM2aNSvf+MY3OrdLpVLa29vzmc98JgceeGCvFgcAAAAAg1WPh4J+5jOfyQEHHJBf/vKXaW1tzYc+9KE8+OCDeeqpp3Lbbbf1RY0AAAAAMOj0uMfa7rvvnvvuuy9/93d/l0MPPTTNzc2ZM2dO7rnnnrzyla/sixoBAAAAYNAplcvl8kAXMdAaGxtTX1+fhoaG1NXVDXQ5AAAAAAyQnuREPe6xliRr167NJZdckve97315//vfn89+9rN56qmnenydpUuXZo899khdXV3q6uqy77775kc/+lHn8XK5nHPPPTeTJk3K6NGjc8ABB+TBBx/sco1169bl1FNPzc4775za2tocc8wx+cMf/lDktgAAAACg23ocrN1yyy3ZZZdd8oUvfCFr167NU089lS984QvZZZddcsstt/ToWpMnT86FF16YX/7yl/nlL3+Zgw46KLNnz+4Mzy6++OIsWrQoX/ziF3PnnXdmwoQJOfTQQ/P00093XuO0007L8uXLc+WVV2bFihVpamrKUUcdlba2tp7eGgAAAAB0W4+Hgk6bNi377bdfli5dmsrKyiRJW1tb5s2bl9tuuy0PPPDANhW044475jOf+Uze+973ZtKkSTnttNPy4Q9/OElH77Tx48fnoosuysknn5yGhoa89KUvzTe/+c2ccMIJSZInn3wyU6ZMyQ9/+MMcfvjh3fqZhoICAAAAkPTxUNDf//73OeOMMzpDtSSprKzMggUL8vvf/77n1f6ftra2XHnllWlubs6+++6bRx55JKtWrcphhx3W2WbUqFF585vfnJ///OdJkrvuuivr16/v0mbSpEmZNm1aZ5tNWbduXRobG7u8AAAAAKAnehysveENb8hDDz200f6HHnoor3/963tcwP33358xY8Zk1KhRmTt3bpYvX57dd989q1atSpKMHz++S/vx48d3Hlu1alVqamqyww47bLbNplxwwQWpr6/vfE2ZMqXHdQMAAAAwslX19IQPfOAD+eAHP5jf/e532WeffZIkd9xxR770pS/lwgsvzH333dfZdo899tjq9f72b/829957b/7617/mqquuyrvf/e4uc7WVSqUu7cvl8kb7Xmxrbc4888wsWLCgc7uxsVG4BgAAAECP9DhYe/vb354k+dCHPrTJY6VSqTPY6s4CAjU1NXnVq16VJNl7771z55135vOf/3znvGqrVq3KxIkTO9uvWbOmsxfbhAkT0tramrVr13bptbZmzZrst99+m/2Zo0aNyqhRo7pxtwAAAACwaT0O1h555JG+qKNTuVzOunXrsssuu2TChAm54YYbsueeeyZJWltbc8stt+Siiy5Kkuy1116prq7ODTfckOOPPz5JsnLlyjzwwAO5+OKL+7ROAAAAAEa2HgdrU6dO7bUfftZZZ+XII4/MlClT8vTTT+fKK6/MzTffnOuuuy6lUimnnXZazj///Oy6667Zddddc/7552e77bbLiSeemCSpr6/P+973vpxxxhnZaaedsuOOO2bhwoWZPn16DjnkkF6rEwAAAABerMfB2je+8Y0tHn/Xu97V7WutXr0673znO7Ny5crU19dnjz32yHXXXZdDDz00Scdw05aWlsybNy9r167Nm970plx//fUZO3Zs5zUWL16cqqqqHH/88WlpacnBBx+cK664osuqpQAAAADQ20rlcrnckxNevALn+vXr88wzz6SmpibbbbddnnrqqV4tsD80Njamvr4+DQ0NqaurG+hyAAAAABggPcmJKnp68bVr13Z5NTU15Te/+U1mzpyZf//3fy9cNAAAAAAMJT0O1jZl1113zYUXXpgPfvCDvXE5AAAAABj0eiVYS5LKyso8+eSTvXU5AAAAABjUerx4wfe///0u2+VyOStXrswXv/jFzJgxo9cKAwAAAIDBrMfB2rHHHttlu1Qq5aUvfWkOOuigfPazn+2tugAAAABgUOtxsNbe3t4XdQAAAADAkNJrc6wtW7Yse+yxR29dDgAAAAAGtR4Fa1/96lfzj//4jznxxBNzxx13JEluuumm7LnnnnnHO96Rfffdt0+KBAAAAIDBptvB2iWXXJL58+fnkUceyTXXXJODDz44559/fo4//vgce+yxefzxx/PlL3+5L2sFAAAAgEGj23OsXXbZZbn00kvz3ve+NzfffHMOOuig3HTTTfnd736X7bffvg9LBAAAAIDBp9s91h577LEccsghSZIDDjgg1dXV+fSnPy1UAwAAAGBE6naw9uyzz+YlL3lJ53ZNTU1e+tKX9klRAAAAADDYdXsoaJJ87Wtfy5gxY5IkGzZsyBVXXJGdd965S5sPfOADvVcdAAAAAAxSpXK5XO5Ow5e//OUplUpbvliplP/93//tlcL6U2NjY+rr69PQ0JC6urqBLgcAAACAAdKTnKjbPdYeffTRba0LAAAAAIaNbs+xBgAAAAA8T7AGAPSplpZk9eqOdwAAGE4EawBAn1ixIpkzJxkzJpkwoeN9zpzkttsGujIAAOgdgjUAoNctXZrMmpVce23S3t6xr729Y3v//ZNLLx3Y+gAAoDcI1gCAXrViRTJ/flIuJxs2dD22YUPH/nnz9FwDAGDo6/aqoC/U3t6e3/3ud1mzZk3an/s19P+ZNWtWrxQGAAxNixYllZUbh2ovVFmZLF6czJjRf3UBAEBv63Gwdscdd+TEE0/MY489lnK53OVYqVRKW1tbrxUHAAwtLS3JNdc8P/xzczZsSJYv72g/enT/1AYAAL2tx8Ha3Llzs/fee+cHP/hBJk6cmFKp1Bd1AQBDUGPj1kO157S3d7QXrAEAMFT1OFh7+OGH85//+Z951ate1Rf1AABDWF1dUlHRvXCtoqKjPQAADFU9XrzgTW96U373u9/1RS0AwBA3enQye3ZStZVf3VVVJccdp7caAABDW497rJ166qk544wzsmrVqkyfPj3V1dVdju+xxx69VhwAMPQsWJBcffWW27S1Jaef3i/lAABAnymVX7wCwVZUVGzcya1UKqVcLg/ZxQsaGxtTX1+fhoaG1BmTAgDb7NJLk3nzNl4dtKqqI1RbsiSZO3fg6gMAgM3pSU7U4x5rjzzySOHCAICRYe7cZPr0ZPHijtU/29s75lSbPbujp9qMGQNdIQAAbLseB2tTp07tizoAgGFmxoyOV0tLx+qfdXXmVAMAYHjpcbD2nF//+td5/PHH09ra2mX/Mcccs81FAQDDx+jRAjUAAIanHgdr//u//5vjjjsu999/f+fcaknHPGtJhuQcawAAAADQUxuvRLAVH/zgB7PLLrtk9erV2W677fLggw/mZz/7Wfbee+/cfPPNfVAiAAAAAAw+Pe6xdvvtt+emm27KS1/60lRUVKSioiIzZ87MBRdckA984AO55557+qJOAAAAABhUetxjra2tLWPGjEmS7LzzznnyySeTdCxq8Jvf/KZ3qwMAAACAQarHPdamTZuW++67L694xSvypje9KRdffHFqamryla98Ja94xSv6okYAAAAAGHR6HKx99KMfTXNzc5LkU5/6VI466qjsv//+2WmnnfLd73631wsEAAAAgMGoVH5uWc9t8NRTT2WHHXboXBl0qGlsbEx9fX0aGhpSV1c30OUAAAAAMEB6khP1uMfapuy44469cRkAAAAAGDK6FazNmTMnV1xxRerq6jJnzpwttl22bFmvFAYAAAAAg1m3grX6+vrOYZ719fV9WhAAAAAADAW9MsfaUGeONQAAAACSnuVEFf1UEwAAAAAMK90aCrrnnnt2e8XPu+++e5sKAgAAAIChoFvB2rHHHtv5+dlnn82SJUuy++67Z999902S3HHHHXnwwQczb968PikSAAAAAAabbgVr55xzTufn97///fnABz6QT37ykxu1eeKJJ3q3OgAAAAAYpHq8eEF9fX1++ctfZtddd+2y/+GHH87ee++dhoaGXi2wP1i8AAAAAICkjxcvGD16dFasWLHR/hUrVuQlL3lJTy8HAAxzLS3J6tUd7wAAMJx0ayjoC5122mn5l3/5l9x1113ZZ599knTMsfZv//Zv+fjHP97rBQIAQ9OKFcmiRck11yTt7UlFRTJ7dnLGGcmMGQNdHQAAbLseDwVNkv/4j//I5z//+Tz00ENJkte85jX54Ac/mOOPP77XC+wPhoICQO9aujSZPz+prEw2bHh+f1VV0taWLFmSzJ07cPUBAMDm9CQnKhSsDTeCNQDoPStWJLNmJVv6hlEqJbfequcaAACDT09yoh4PBX1Oa2tr1qxZk/b29i77/+Zv/qboJQGAYWDRoo17qr1YZWWyeLFgDQCAoa3HwdrDDz+c9773vfn5z3/eZX+5XE6pVEpbW1uvFQcADC0tLc/PqbYlGzYky5d3tB89un9qAwCA3tbjYO2kk05KVVVV/uu//isTJ05MqVTqi7oAgCGosXHrodpz2ts72gvWAAAYqnocrN17772566678upXv7ov6gEAhrC6uo7VP7sTrlVUdLQHAIChqqKnJ+y+++7585//3Be1AABD3OjRyezZHat/bklVVXLccXqrAQAwtPU4WLvooovyoQ99KDfffHP+8pe/pLGxscsLABjZFixItjblaltbcvrp/VMPAAD0lVK5XC735ISKio4s7sVzqw3lxQt6sowqALB1l16azJu38eqgVVUdodqSJcncuQNXHwAAbE5PcqIez7H205/+tHBhAMDIMHduMn16snhxx+qf7e0dc6rNnt3RU23GjIGuEAAAtl2Pe6wNR3qsAUDfaWnpWP2zrs6cagAADH590mPtvvvu61a7PfbYo7uXBABG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rN1yyy2ZP39+7rjjjtxwww3ZsGFDDjvssDQ3N3e2ufjii7No0aJ88YtfzJ133pkJEybk0EMPzdNPP93Z5rTTTsvy5ctz5ZVXZsWKFWlqaspRRx2Vtra2gbitEWXFimT+/KRcTjZs6Hpsw4aO/fPm6bkGAAAADD+lcrlcHuginvOnP/0p48aNyy233JJZs2alXC5n0qRJOe200/LhD384SUfvtPHjx+eiiy7KySefnIaGhrz0pS/NN7/5zZxwwglJkieffDJTpkzJD3/4wxx++OFb/bmNjY2pr69PQ0ND6urq+vQeh5s5czp6pr04VHuhqqpk9uzkP/+z/+oCAAAAKKInOdGgmmOtoaEhSbLjjjsmSR555JGsWrUqhx12WGebUaNG5c1vfnN+/vOfJ0nuuuuurF+/vkubSZMmZdq0aZ1tXmzdunVpbGzs8qLnWlqSa67ZcqiWdBxfvtyCBgAAAMDwMmiCtXK5nAULFmTmzJmZNm1akmTVqlVJkvHjx3dpO378+M5jq1atSk1NTXbYYYfNtnmxCy64IPX19Z2vKVOm9PbtjAiNjc/PqbY17e0d7QEAAACGi0ETrJ1yyim577778u///u8bHSuVSl22y+XyRvtebEttzjzzzDQ0NHS+nnjiieKFj2B1dUlFN5+gioqO9gAAAADDxaAI1k499dR8//vfz09/+tNMnjy5c/+ECROSZKOeZ2vWrOnsxTZhwoS0trZm7dq1m23zYqNGjUpdXV2XFz03enTH3GlVVVtuV1WVHHdcR3sAAACA4WJAg7VyuZxTTjkly5Yty0033ZRddtmly/FddtklEyZMyA033NC5r7W1Nbfcckv222+/JMlee+2V6urqLm1WrlyZBx54oLMNfWfBgmRri6+2tSWnn94/9QAAAAD0l630Nepb8+fPz3e+851cc801GTt2bGfPtPr6+owePTqlUimnnXZazj///Oy6667Zddddc/7552e77bbLiSee2Nn2fe97X84444zstNNO2XHHHbNw4cJMnz49hxxyyEDe3ogwc2ayZEkyb15SWdl1IYOqqo5QbcmSZMaMgasRAAAAoC8MaLC2dOnSJMkBBxzQZf/ll1+ek046KUnyoQ99KC0tLZk3b17Wrl2bN73pTbn++uszduzYzvaLFy9OVVVVjj/++LS0tOTggw/OFVdckcrKyv66lRFt7txk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YyPNzc153etely9+8YsbHXvmmWdy991352Mf+1juvvvuLFu2LL/97W9zzDHHdGl32mmnZfny5bnyyiuzYsWKNDU15aijjkpbW1tnmxNPPDH33ntvrrvuulx33XW599578853vrPP74+Bs6Vn64Wuvvrq/Pd//3cmTZq00THPFpuytWfr97//fWbOnJlXv/rVufnmm/OrX/0qH/vYx/KSl7yks41ni03Z2rN1+umn57rrrsu3vvWtPPTQQzn99NNz6qmn5pprruls49liU2655ZbMnz8/d9xxR2644YZs2LAhhx12WJqbmzvbXHzxxVm0aFG++MUv5s4778yECRNy6KGH5umnn+5s4/nixbb2bPk+T1Hd+XfrOb7P0xPdebYG9ff5MmxBkvLy5cu32OYXv/hFOUn5scceK5fL5fJf//rXcnV1dfnKK6/sbPPHP/6xXFFRUb7uuuvK5XK5/Otf/7qcpHzHHXd0trn99tvLScr/8z//0/s3wqCzuWfrD3/4Q/llL3tZ+YEHHihPnTq1vHjx4s5jni26Y1PP1gknnFB+xzvesdlzPFt0x6aerde+9rXlT3ziE132veENbyh/9KMfLZfLni26b82aNeUk5VtuuaVcLpfL7e3t5QkTJpQvvPDCzjbPPvtsub6+vnzppZeWy2XPF93z4mdrU3yfp4jNPVu+z7OtNvVsDebv83qssc0aGhpSKpWy/fbbJ0nuuuuurF+/Pocddlhnm0mTJmXatGn5+c9/niS5/fbbU19fnze96U2dbfbZZ5/U19d3tmHkaW9vzzvf+c7867/+a1772tdudNyzRRHt7e35wQ9+kN122y2HH354xo0blze96U1dhvR5tihq5syZ+f73v58//vGPKZfL+elPf5rf/va3Ofzww5N4tui+hoaGJMmOO+6YJHnkkUeyatWqLs/OqFGj8uY3v7nzufB80R0vfrY218b3eXpqU8+W7/P0hhc/W4P9+7xgjW3y7LPP5iMf+UhOPPHE1NXVJUlWrVqVmpqa7LDDDl3ajh8/PqtWrepsM27cuI2uN27cuM42jDwXXXRRqqqq8oEPfGCTxz1bFLFmzZo0NTXlwgsvzBFHHJHrr78+xx13XObMmZNbbrkliWeL4r7whS9k9913z+TJk1NTU5MjjjgiS5YsycyZM5N4tuiecrmcBQsWZObMmZk2bVqSdP7d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\n",
      "text/plain": [
       "<Figure size 1500x1000 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plot_scatter_chart(df8,\"Rajaji Nagar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "4803b802",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABNYAAANVCAYAAAC09nNHAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQGoP6dpAAB3M0lEQVR4nOzde5icdX0//PfsbhKWXXbllGxSYhoL+BMDaEU5JERADlJRJCqK1YLVVkhAIfCgaBXSWgJqQ+2FCZ5+orYWW01ARBEUwQSl5fhw0PJAGwElBwTcZZclye7O88c0C5vjzmR3Z3bzel3Xfe19+N73fGY6HfWd76FQLBaLAQAAAADKUlftAgAAAABgNBKsAQAAAEAFBGsAAAAAUAHBGgAAAABUQLAGAAAAABUQrAEAAABABQRrAAAAAFABwRoAAAAAVECwBgAAAAAVEKwBANSwq6++OoVCIXfdddcWr5900kn54z/+47Kfe9RRR2XGjBnbbfeb3/wmhUIhn//858t+je098+qrrx6yZwIAVINgDQAAAAAqIFgDAAAAgAoI1gAAxpBisZjFixfnNa95TRobG7P77rvnne98Z/7nf/5ni+2XL1+eww47LI2NjfmjP/qjfOpTn0pvb+9m7fr6+vL3f//3efnLX55ddtklhxxySH76058OaPPoo4/mAx/4QPbbb7/suuuu+aM/+qO89a1vzQMPPDAs7xUAoNoEawAAo0Bvb296eno224rF4oB2H/7wh3Puuefm2GOPzbXXXpvFixfnoYceyhFHHJE1a9YMaLt69eq85z3vyZ//+Z/nuuuuyzvf+c585jOfyUc/+tHNXv/KK6/MjTfemH/8x3/MP//zP6euri4nnnhifvnLX/a3efLJJ7Pnnnvmsssuy4033pgvfvGLaWhoyKGHHpqHH354eD4YAIAqaqh2AQAAbN9hhx221WvTpk1Lktxxxx35yle+kn/4h3/I/Pnz+68feeSR2X///bNo0aJcfvnl/eeffvrpXHfddXnb296WJDn++OPT3d2dJUuW5MILL8zLX/7y/ra9vb25+eabs8suuyRJTjjhhPzxH/9xPv3pT+fmm29OksyePTuzZ88ecM9b3vKWvPrVr86XvvSlLFq0aAg+CQCA2qHHGgDAKPDNb34zd95552bbrFmz+tv84Ac/SKFQyPve974Bvdra2tpy8MEH59Zbbx3wzN12260/VNvove99b/r6+vLzn/98wPk5c+b0h2ob733rW9+an//85/1DR3t6enLppZfmgAMOyPjx49PQ0JDx48fnkUceya9//esh/kQAAKpPjzUAgFHgVa96VQ455JDNzre2tuaJJ55IkqxZsybFYjGTJk3a4jNe8YpXDDjeUru2trYkpd5sWzq/6bn169ens7Mzra2tmT9/fr74xS/mYx/7WN74xjdm9913T11dXT70oQ+lu7t7cG8UAGAUEawBAIwRe+21VwqFQpYvX54JEyZsdn3Tc5vOuZaU5l1Lkj333HOL5zc9N378+DQ3NydJ/vmf/zl/8Rd/kUsvvXRAu9///vd52cteVtZ7AQAYDQwFBQAYI0466aQUi8X87ne/yyGHHLLZduCBBw5o/9xzz+X73//+gHPf/va3U1dXN2CutCRZunRpXnjhhQH3Xn/99TnyyCNTX1+fJCkUCpuFdzfccEN+97vfDeXbBACoGXqsAQCMETNnzsxf//Vf5wMf+EDuuuuuzJ49O01NTVm1alVWrFiRAw88MGeddVZ/+z333DNnnXVWHn/88ey///754Q9/mK985Ss566yzBixckCT19fU57rjjMn/+/PT19eXyyy9PR0dHFixY0N/mpJNOytVXX53/83/+Tw466KDcfffd+dznPpd99tlnxD4DAICRJFgDABhDvvSlL+Wwww7Ll770pSxevDh9fX2ZMmVKZs6cmTe84Q0D2ra1teWLX/xiLrjggjzwwAPZY4898olPfGJAWLbR2WefnRdeeCEf+chHsnbt2rz61a/ODTfckJkzZ/a3+cIXvpBx48Zl4cKF6ezszJ/+6Z9m6dKl+Zu/+Zthf98AANVQKBaLxWoXAQAAAACjjTnWAAAAAKACgjUAAAAAqIBgDQAAAAAqIFgDAAAAgAoI1gAAAACgAoI1AAAAAKhAQ7ULqAV9fX158skns9tuu6VQKFS7HAAAAACqpFgs5rnnnsuUKVNSV7ftPmmCtSRPPvlkpk6dWu0yAAAAAKgRTzzxRPbZZ59tthGsJdltt92SlD6wlpaWKlcDAAAAQLV0dHRk6tSp/XnRtgjWkv7hny0tLYI1AAAAAAY1XZjFCwAAAACgAoI1AAAAAKiAYA0AAAAAKmCOtUEqFovp6elJb29vtUsZs+rr69PQ0DCoMcwAAAAA1SZYG4T169dn1apVef7556tdypi36667ZvLkyRk/fny1SwEAAADYJsHadvT19WXlypWpr6/PlClTMn78eD2qhkGxWMz69evz1FNPZeXKldlvv/1SV2ekMgAAAFC7BGvbsX79+vT19WXq1KnZddddq13OmNbY2Jhx48blsccey/r167PLLrtUuyQAAACArdIlaJD0nhoZPmcAAABgtJBiAAAAAEAFBGsAAAAAUAHBGgAAAABUQLA2grq7kzVrSn+H28KFC/P6178+u+22WyZOnJi3v/3tefjhh7d5z9VXX51CodC/NTc353Wve12WLl06oN1RRx2Vc889d4v3v+xlL9vqcZL8+te/zj777JM5c+Zk3bp1lb49AAAAgKoTrI2AFSuSOXOS5uakra30d86c5Pbbh+81b7vttsybNy933HFHbr755vT09OT4449PV1fXNu9raWnJqlWrsmrVqtx777054YQTcuqpp243lBuMO++8M0ceeWROOOGE/Pu//3smTJiww88EAAAAqBbB2jBbsiSZPTu5/vqkr690rq+vdHzkkclVVw3P6954440544wz8upXvzoHH3xwvv71r+fxxx/P3Xffvc37CoVC2tra0tbWlv322y+f+cxnUldXl/vvv3+H6rnllltyzDHH5AMf+EC+9rWvpb6+foeeBwAAAFBtgrVhtGJFMm9eUiwmPT0Dr/X0lM7PnTu8Pdc2am9vT5Lsscceg76nt7c33/jGN5Ikf/qnf1rxay9btixvectb8slPfjKf+9znKn4OAAAAQC1pqHYBY9miRUl9/eah2kvV1ydXXJHMnDl8dRSLxcyfPz+zZs3KjBkzttm2vb09zc3NSZLu7u6MGzcuX/7yl/Mnf/InA9otXrw4X/3qVwec6+npyS677DLgXGdnZ971rnflE5/4RD7+8Y8PwbsBAAAAqA2CtWHS3Z1cd92Lwz+3pqcnWbas1L6xcXhqOfvss3P//fdnxYoV222722675Z577kmSPP/88/nJT36SD3/4w9lzzz3z1re+tb/dn//5n+eTn/zkgHuXLl2aSy+9dMC5xsbGzJo1K1/5yldy2mmn5VWvetUQvCMAAACA6hOsDZOOju2Hahv19ZXaD0ewds455+T73/9+fv7zn2efffbZbvu6urrsu+++/ccHHXRQbrrpplx++eUDgrXW1tYB7ZJk4sSJmz2vvr4+1157bd7xjnfk6KOPzi233JIDDjhgB94RAAAAQG0wx9owaWlJ6gb56dbVldoPpWKxmLPPPjtLly7NLbfckunTp1f8rPr6+nR3d1d8/4QJE7J06dK84Q1vyNFHH50HH3yw4mcBAAAA1ArB2jBpbExOPjlp2E6fwIaG5JRThr632rx58/LP//zP+fa3v53ddtstq1evzurVq7cbkBWLxf62K1euzJe//OX8+Mc/zsknn7xD9YwfPz7f+973csQRR+SYY47JAw88sEPPAwAAAKg2wdowmj8/6e3ddpve3uS884b+tZcsWZL29vYcddRRmTx5cv/2ne98Z5v3dXR09Ld91atelX/4h3/I3/7t3242n1olxo0bl3/7t3/L7Nmzc8wxx+T+++/f4WcCAAAAVEuhWCwWq11EtXV0dKS1tTXt7e1p2WRM5gsvvJCVK1dm+vTpm614ORhXXZXMnbv56qANDaVQbfHi5Mwzd/QdjB07+nkDAAAA7Iht5USb0mNtmJ15ZrJ8eWlY6MY51+rqSsfLlwvVAAAAAEYrq4KOgJkzS1t3d2n1z5aW4VkBFAAAAICRI1gbQY2NAjUAAACAscJQUAAAAACogGANAAAAACogWAMAAACgIl3ru1JYUEhhQSFd67uqXc6IE6wBAAAAQAUEawAAAABQAauCAgAAADBoLx3y2bVhy/tJ0jS+acRqqhbBGgAAAACD1ryweYvnJ31+0oDj4sXFkSinqgwFHaOWLFmSgw46KC0tLWlpacnhhx+eH/3oR9u85+qrr06hUOjfmpub87rXvS5Lly4d0O6oo47Kueeeu8X7X/ayl231OEl+/etfZ5999smcOXOybt26St8eAAAAQNXpsTZCutZ39Se6nRd1Dnt3yH322SeXXXZZ9t133yTJN77xjZx88sm599578+pXv3qr97W0tOThhx9Okjz33HP5+te/nlNPPTUPPfRQXvnKV+5QTXfeeWdOPPHEnHzyyfnyl7+c+vr6HXoeAAAAMPI6L+rs3+/a0NXfU23NBWvSNG7sD/98KT3Wxqi3vvWt+bM/+7Psv//+2X///fP3f//3aW5uzh133LHN+wqFQtra2tLW1pb99tsvn/nMZ1JXV5f7779/h+q55ZZbcswxx+QDH/hAvva1rwnVAAAAYJRqGt/04vaSIK1pXNOAazsDwdpOoLe3N9dcc026urpy+OGHl3XfN77xjSTJn/7pn1b8+suWLctb3vKWfPKTn8znPve5ip8DAAAAUEsMBR1G1V4l44EHHsjhhx+eF154Ic3NzVm2bFkOOOCAbd7T3t6e5ubSkNXu7u6MGzcuX/7yl/Mnf/InA9otXrw4X/3qVwec6+npyS677DLgXGdnZ971rnflE5/4RD7+8Y8PwbsCAAAAqA2CtWFU7VUyXvnKV+a+++7LH/7wh3zve9/L6aefnttuu22b4dpuu+2We+65J0ny/PPP5yc/+Uk+/OEPZ88998xb3/rW/nZ//ud/nk9+8pMD7l26dGkuvfTSAecaGxsza9asfOUrX8lpp52WV73qVUP4DgEAAIBqahrftFOs/rk1grUxbPz48f2LFxxyyCG5884784UvfCFf+tKXtnpPXV1d/z1JctBBB+Wmm27K5ZdfPiBYa21tHdAuSSZOnLjZ8+rr63PttdfmHe94R44++ujccsst2+01BwAAADAaCNaGUa2tklEsFrNu3bqy76uvr093d3fFrzthwoQsXbo073znO3P00Ufnpz/9aWbMmFHx8wAAAABqgWBtGG1t7rSNq2QMp0984hM58cQTM3Xq1Dz33HO55pprcuutt+bGG2/c5n3FYjGrV69OUppj7eabb86Pf/zjfPrTn96hesaPH5/vfe97OfXUU3PMMcfkpz/9aQ488MAdeiYAAABANQnWxqg1a9bk/e9/f1atWpXW1tYcdNBBufHGG3Pcccdt876Ojo5Mnjw5Samn2bRp0/K3f/u3+djHPrbDNY0bNy7/9m//ltNOO60/XDvooIN2+LkAAAAA1VAoFos77wxz/6ujoyOtra1pb29PS0vLgGsvvPBCVq5cmenTp2+24mU5utZ39S9m0HlR57D3WButhurzBgAAAKjEtnKiTemxNkJ29lUyAAAAAMaaumoXAAAAAACjkWANAAAAACogWAMAAACACgjWBskaDyPD5wwAAACMFoK17Rg3blyS5Pnnn69yJTuHjZ/zxs8dAAAAoFZZFXQ76uvr87KXvSxr165Nkuy6664pFApVrmrsKRaLef7557N27dq87GUvS319fbVLAgAAANgmwdogtLW1JUl/uMbwednLXtb/eQMAAADUMsHaIBQKhUyePDkTJ07Mhg0bql3OmDVu3Dg91QAAAIBRQ7BWhvr6esEPAAAAAEksXgAAAAAA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AAAAFRCsAQAAAEAFBGsAAAAAUAHBGgAAAABUQLAGAAAAABUQrAEAAABABQRrAAAAAFABwRoAAAAAVECwBgDAmNa1viuFBYUUFhTStb6r2uUAAGOIYA0AAAAAKiBYAwAAAIAKNFS7AAAAGGovHfLZtWHL+0nSNL5pxGoCAMYewRoAAGNO88LmLZ6f9PlJA46LFxdHohwAYIwyFBQAAAAAKqDHGgAAY07nRZ39+10buvp7qq25YE2axhn+CQAMDcEaAABjztbmTmsa12ReNQBgyBgKCgAAAAAVEKwBAAAAQAXKGgra3t6eZcuWZfny5fnNb36T559/PnvvvXde+9rX5oQTTsgRRxwxXHUCAEBFmsY3Wf0TABgWg+qxtmrVqvzVX/1VJk+enL/9279NV1dXXvOa1+RNb3pT9tlnn/zsZz/LcccdlwMOOCDf+c53hrtmAAAAAKi6QfVYO/jgg/MXf/EX+c///M/MmDFji226u7tz7bXXZtGiRXniiSdywQUXDGmhAAAAAFBLCsVicbv94p966qnsvffeg35oue2rraOjI62trWlvb09LS0u1ywEAAACgSsrJiQY1FLTckGw0hWoAAAAAUImyVwX9xje+kRtuuKH/+MILL8zLXvayHHHEEXnssceGtDgAAAAAqFVlB2uXXnppGhsbkyS//OUvc+WVV+azn/1s9tprr5x33nlDXiAAAAAA1KJBLV7wUk888UT23XffJMm1116bd77znfnrv/7rzJw5M0cdddRQ1wcAAAAANansHmvNzc15+umnkyQ33XRTjj322CTJLrvsku7u7qGtDgAAAABqVNk91o477rh86EMfymtf+9r8f//f/5e3vOUtSZKHHnoof/zHfzzU9QEAAABATSq7x9oXv/jFHH744Xnqqafyve99L3vuuWeS5O67785pp5025AUCAAAAQC0qFIvFYrWLqLaOjo60tramvb09LS0t1S4HAAAAgCopJycqu8dakixfvjzve9/7csQRR+R3v/tdkuRb3/pWVqxYUcnjAAAAAGDUKTtY+973vpcTTjghjY2Nueeee7Ju3bokyXPPPZdLL710yAsEAAAAgFpUdrD2mc98JldddVW+8pWvZNy4cf3njzjiiNxzzz1DWhwAAAAA1Kqyg7WHH344s2fP3ux8S0tL/vCHPwxFTQAAAABQ88oO1iZPnpxHH310s/MrVqzIK17xiiEpCgAAAABqXdnB2oc//OF89KMfzX/8x3+kUCjkySefzL/8y7/kggsuyNy5c4ejRgAAAACoOQ3l3nDhhRemvb09Rx99dF544YXMnj07EyZMyAUXXJCzzz57OGoEAAAAgJpTKBaLxUpufP755/OrX/0qfX19OeCAA9Lc3DzUtY2Yjo6OtLa2pr29PS0tLdUuBwAAAIAqKScnKnso6EZPPvlknn766Rx44IFpbm5OhfkcAAAAAIxKZQdrTz/9dN70pjdl//33z5/92Z9l1apVSZIPfehDOf/884e8QAAAAACoRWUHa+edd17GjRuXxx9/PLvuumv/+Xe/+9258cYbh7Q4AAAAAKhVZS9ecNNNN+XHP/5x9tlnnwHn99tvvzz22GNDVhgAAAAA1LKye6x1dXUN6Km20e9///tMmDBhSIoCAAAAgFpXdrA2e/bsfPOb3+w/LhQK6evry+c+97kcffTRQ1ocAAAAANSqsoeCfu5zn8tRRx2Vu+66K+vXr8+FF16Yhx56KM8880xuv/324agRAAAAAGpO2T3WDjjggNx///15wxvekOOOOy5dXV2ZM2dO7r333vzJn/zJcNQIAAAAADWnUCwWi9Uuoto6OjrS2tqa9vb2tLS0VLscAAAAAKqknJyo7KGgSfLss8/ma1/7Wn7961+nUCjkVa96VT7wgQ9kjz32qKhgAAAAABhtyh4Ketttt2X69On5p3/6pzz77LN55pln8k//9E+ZPn16brvttuGoEQAAAABqTtlDQWfMmJEjjjgiS5YsSX19fZKkt7c3c+fOze23354HH3xwWAodToaCAgAAAJCUlxOV3WPtv//7v3P++ef3h2pJUl9fn/nz5+e///u/y68WAAAAAEahsoO1P/3TP82vf/3rzc7/+te/zmte85qhqAkAAAAAal7Zixd85CMfyUc/+tE8+uijOeyww5Ikd9xxR774xS/msssuy/3339/f9qCDDhq6SgEAAACghpQ9x1pd3bY7uRUKhRSLxRQKhfT29u5QcSPFHGsAAAAAJOXlRGX3WFu5cmXFhQEAAADAWFF2sDZt2rThqAMAAAAARpWyg7VvfvOb27z+F3/xFxUXAwAAAACjRdlzrO2+++4Djjds2JDnn38+48ePz6677ppnnnlm0M9auHBhli5dmv/6r/9KY2NjjjjiiFx++eV55Stf2d+mWCxmwYIF+fKXv5xnn302hx56aL74xS/m1a9+dX+bdevW5YILLsi//uu/pru7O29605uyePHi7LPPPoOqwxxrAAAAACTl5UTbXolgC5599tkBW2dnZx5++OHMmjUr//qv/1rWs2677bbMmzcvd9xxR26++eb09PTk+OOPT1dXV3+bz372s1m0aFGuvPLK3HnnnWlra8txxx2X5557rr/Nueeem2XLluWaa67JihUr0tnZmZNOOmnULJ4AAAAMr671XSksKKSwoJCu9V3bv2GEngXA6FZ2j7Wtueuuu/K+970v//Vf/1XxM5566qlMnDgxt912W2bPnp1isZgpU6bk3HPPzcc+9rEkpd5pkyZNyuWXX54Pf/jDaW9vz957751vfetbefe7350kefLJJzN16tT88Ic/zAknnLDd19VjDQAAxrau9V1pXticJOm8qDNN45tq4lkA1J5h7bG2NfX19XnyySd36Bnt7e1Jkj322CNJaQXS1atX5/jjj+9vM2HChLzxjW/ML37xiyTJ3XffnQ0bNgxoM2XKlMyYMaO/zabWrVuXjo6OARsAAAAAlKPsxQu+//3vDzguFotZtWpVrrzyysycObPiQorFYubPn59Zs2ZlxowZSZLVq1cnSSZNmjSg7aRJk/LYY4/1txk/fvxmc79NmjSp//5NLVy4MAsWLKi4VgAAoPa9dJhm14Yt7ycZVI+zoXwWAGNH2cHa29/+9gHHhUIhe++9d4455pj8wz/8Q8WFnH322bn//vuzYsWKza4VCoUBx8VicbNzm9pWm4suuijz58/vP+7o6MjUqVMrqBoAAKhVG4drbmrS5wf+w33x4u3PjjOUzwJg7Cg7WOvr6xvyIs4555x8//vfz89//vMBK3m2tbUlKfVKmzx5cv/5tWvX9vdia2try/r16/Pss88O6LW2du3aHHHEEVt8vQkTJmTChAlD/j4AAAAA2HmUHaxtzdKlS3PJJZfk/vvvH/Q9xWIx55xzTpYtW5Zbb70106dPH3B9+vTpaWtry80335zXvva1SZL169fntttuy+WXX54ked3rXpdx48bl5ptvzqmnnpokWbVqVR588MF89rOfHaJ3BwAAjDadF3X273dt6OrvXbbmgjVpGlfekM2hfBYAY0dZwdpXvvKV3HTTTRk3blw+8pGP5LDDDsstt9yS888/Pw8//HDe//73l/Xi8+bNy7e//e1cd9112W233frnRGttbU1jY2MKhULOPffcXHrppdlvv/2y33775dJLL82uu+6a9773vf1tP/jBD+b888/PnnvumT322CMXXHBBDjzwwBx77LFl1QMAAIwdW5vvrGlcU9lzoQ3lswAYOwYdrH3+85/PJz7xiRx00EH59a9/neuuuy6f/OQns2jRopxzzjmZN29e9tprr7JefMmSJUmSo446asD5r3/96znjjDOSJBdeeGG6u7szd+7cPPvsszn00ENz0003Zbfddutvf8UVV6ShoSGnnnpquru786Y3vSlXX3116uvry6oHAAAAAAarUCwWBzW75qte9ar8P//P/5O//Mu/zK233ppjjjkmxxxzTL773e/mZS972TCXObw6OjrS2tqa9vb2tLS0VLscAABgiHWt7+pfgKDzos4d6mU2lM8CoPaUkxMNusfaY4891j+08qijjsq4cePy93//96M+VAMAgNFCoFO5rvVdA/Z35LNrGt9k9U8AkiR1g234wgsvZJddduk/Hj9+fPbee+9hKQoAAAAAal1Zixd89atfTXNz6V/Ienp6cvXVV282r9pHPvKRoasOAAAAAGrUoIO1l7/85fnKV77Sf9zW1pZvfetbA9oUCgXBGgAADKEBQxg3bHk/2fqqlTuztZ1r+/efev6pLe4nycTmiSNWEwBjy6AXLxjLLF4AAECtKiwoDKqdOb8257MDoBLl5ESDnmMNAAAAAHhRWXOsAQAAI6vzos7+/a4NXZn0+UlJkjUXrEnTOMM/t2XN+Wv69596/qnMWDIjSfLgWQ9m710txAbAjhOsAQBADdva3GlN45rMq7YdW5s7be9d9zavGgBDwlBQAAAAAKiAYA0AAAAAKlDRUNC+vr48+uijWbt2bfr6+gZcmz179pAUBgAADNQ0vskKlhWa2DzRZwfAkCs7WLvjjjvy3ve+N4899liKxYH/wVQoFNLb2ztkxQEAAABArSo7WDvzzDNzyCGH5IYbbsjkyZNTKBSGoy4AAAAAqGllB2uPPPJIvvvd72bfffcdjnoAAAAAYFQoe/GCQw89NI8++uhw1AIAAAAAo0bZPdbOOeecnH/++Vm9enUOPPDAjBs3bsD1gw46aMiKAwAYrbrWd6V5YXOSpPOizjSNb6pyRQAADLWyg7V3vOMdSZK//Mu/7D9XKBRSLBYtXgAAAADATqPsYG3lypXDUQcAAAAAjCplB2vTpk0bjjoAAEa9rvVdL+5v2PJ+EsNCAQDGiLKDtY1+9atf5fHHH8/69esHnH/b2962w0UBAIxGG+dU29Skz08acFy8uDgS5QAAMMzKDtb+53/+J6ecckoeeOCB/rnVktI8a0nMsQYAAADATqHsYO2jH/1opk+fnp/85Cd5xStekf/8z//M008/nfPPPz+f//znh6NGAIBRofOizv79rg1d/T3V1lywJk3jDP8EABhryg7WfvnLX+aWW27J3nvvnbq6utTV1WXWrFlZuHBhPvKRj+Tee+8djjoBAGre1uZOaxrXZF41AIAxqK7cG3p7e9PcXJo/ZK+99sqTTz6ZpLSowcMPPzy01QEAAABAjSq7x9qMGTNy//335xWveEUOPfTQfPazn8348ePz5S9/Oa94xSuGo0YAAAAAqDllB2t/8zd/k66u0pLxn/nMZ3LSSSflyCOPzJ577pnvfOc7Q14gAMBo1DS+yeqfAABjXKG4cVnPHfDMM89k9913718ZdLTp6OhIa2tr2tvb09LSUu1yAAAAAKiScnKisnusbckee+wxFI8BAAAAgFFjUMHanDlzcvXVV6elpSVz5szZZtulS5cOSWEAAAAAUMsGFay1trb2D/NsbW0d1oIAAAAAYDQYkjnWRjtzrAEAAACQlJcT1Y1QTQAAAAAwpgxqKOhrX/vaQa/4ec899+xQQQAAAAAwGgwqWHv729/ev//CCy9k8eLFOeCAA3L44YcnSe6444489NBDmTt37rAUCQAAAAC1ZlDB2sUXX9y//6EPfSgf+chH8nd/93ebtXniiSeGtjoAAAAAqFFlL17Q2tqau+66K/vtt9+A84888kgOOeSQtLe3D2mBI8HiBQAAAAAkw7x4QWNjY1asWLHZ+RUrVmSXXXYp93EAAAAAMCoNaijoS5177rk566yzcvfdd+ewww5LUppj7f/+3/+bT3/600NeIAAAAADUorKDtY9//ON5xStekS984Qv59re/nSR51atelauvvjqnnnrqkBcIAABsXdf6rjQvbE6SdF7UmabxTVWuCAB2HmUHa0ly6qmnCtEAAAAA2KlVFKwlyfr167N27dr09fUNOP/yl798h4sCAAAAgFpXdrD2yCOP5C//8i/zi1/8YsD5YrGYQqGQ3t7eISsOAADYXNf6rhf3N2x5P4lhoQAwzMoO1s4444w0NDTkBz/4QSZPnpxCoTAcdQEAAFuxcU61TU36/KQBx8WLiyNRDgDstMoO1u67777cfffd+T//5/8MRz0AAAAAMCqUHawdcMAB+f3vfz8ctQAAAIPQeVFn/37Xhq7+nmprLliTpnGGfwLASKkr94bLL788F154YW699dY8/fTT6ejoGLABAADDq2l804vbS4K0pnFNA64BAMOr7B5rxx57bJLkTW9604DzFi8AAAAAYGdSdrD2s5/9bDjqAAAAAIBRpexg7Y1vfONw1AEAAFSgaXyT1T8BoEoGHazdf//9g2p30EEHVVwMAAAAAIwWgw7WXvOa16RQKKRY3Pq/hpljDQAAAICdxaCDtZUrVw5nHQAADJOu9V1pXticJOm8qNNqkQAAQ2TQwdq0adOGsw4AAAAAGFXqql0AAAAAAIxGZa8KCgBA7eta3/Xi/oYt7ycxLBQAYAcI1gAAxqCNc6ptatLnJw04Ll689YWpAADYNkNBAQAAAKACeqwBAIxBnRd19u93bejq76m25oI1aRpn+CcAwFAou8famjVr8v73vz9TpkxJQ0ND6uvrB2wAAFRf0/imF7eXBGlN45oGXAMAoHJl91g744wz8vjjj+dTn/pUJk+enEKhMBx1AQAAAEBNKztYW7FiRZYvX57XvOY1w1AOAAAAAIwOZQdrU6dOTbFo9SgAgNGiaXyT1T8BAIZB2XOs/eM//mM+/vGP5ze/+c0wlAMAAAAAo8OgeqztvvvuA+ZS6+rqyp/8yZ9k1113zbhx4wa0feaZZ4a2QgAAAACoQYMK1v7xH/9xmMsAAAAAgNFlUMHa6aefPqiHdXd371AxAAAAADBalD3H2rx587Z4vqurKyeeeOIOFwQAAAAAo0HZwdpNN92Uv/mbvxlwrqurK29+85vT29s7ZIUBAAAAQC0b1FDQl7rpppsya9as7LnnnjnvvPPy3HPP5YQTTkhDQ0N+9KMfDUeNAAAAAFBzyg7Wpk+fnh//+Mc56qijUldXl2uuuSYTJkzIDTfckKampuGoEQAAAABqTtnBWpLMmDEjP/jBD3Lsscfm0EMPzQ9+8IM0NjYOdW0AAAAAULMGFay99rWvTaFQ2Oz8hAkT8uSTT2bmzJn95+65556hqw4AAAAAatSggrW3v/3tw1wGAAAAAIwuhWKxWKx2EdXW0dGR1tbWtLe3p6WlpdrlAAAAAFAl5eREdSNUEwAAAACMKWUvXtDb25srrrgi//Zv/5bHH38869evH3D9mWeeGbLiAAAAAKBWld1jbcGCBVm0aFFOPfXUtLe3Z/78+ZkzZ07q6upyySWXDEOJAACjU9f6rhQWFFJYUEjX+q5qlwMAwBArO1j7l3/5l3zlK1/JBRdckIaGhpx22mn56le/mk9/+tO54447hqNGAAAAAKg5ZQdrq1evzoEHHpgkaW5uTnt7e5LkpJNOyg033DC01QEAAABAjSo7WNtnn32yatWqJMm+++6bm266KUly5513ZsKECUNbHQDAKNO1vuvFbcOLwz+7NnQNuAYAwOhX9uIFp5xySn7605/m0EMPzUc/+tGcdtpp+drXvpbHH38855133nDUCAAwajQvbN7i+UmfnzTguHhxcSTKAQBgGJUdrF122WX9++985zszderU3H777dl3333ztre9bUiLAwAAAIBaVSgWi0Pyz6Vr1qzJl770pXz6058eiseNqI6OjrS2tqa9vT0tLS3VLgcAGMVeOsyza0NXf0+1NResSdO4pv5rTeObNrsXAIDqKycnKnuOta1ZvXp1FixYMFSPAwAYlZrGN724vTRIG9c04BoAAKPfkAVrAAAAALAzEawBAAAAQAXKXrwAAIDBaRrfZPVPAIAxbNDB2vz587d5/amnntrhYgAAAABgtBh0sHbvvfdut83s2bN3qBgAAAAAGC0GHaz97Gc/G846AAAAAGBUsXgBAAAAAFRgUMHaZZddlq6urkE98D/+4z9yww037FBRAAAAAFDrBhWs/epXv8q0adNy1lln5Uc/+tGAhQp6enpy//33Z/HixTniiCPynve8Jy0tLcNWMAAAAADUgkHNsfbNb34z999/f774xS/mz//8z9Pe3p76+vpMmDAhzz//fJLkta99bf76r/86p59+eiZMmDCsRQMAAABAtRWKxWKxnBuKxWLuv//+/OY3v0l3d3f22muvvOY1r8lee+01XDUOu46OjrS2tqa9vV1vOwAAAICdWDk50aBXBd2oUCjk4IMPzsEHH1xxgQAAAAAw2lkVFAAAAAAqIFgDAAAAgAoI1gAAAACgAoI1AAAAAKhAxcHao48+mh//+Mfp7u5OUlotFAAAAAB2FmUHa08//XSOPfbY7L///vmzP/uzrFq1KknyoQ99KOeff/6QFwgAY1HX+q4UFhRSWFBI1/quapcDAABUoOxg7bzzzktDQ0Mef/zx7Lrrrv3n3/3ud+fGG28c0uIAAAAAoFY1lHvDTTfdlB//+MfZZ599Bpzfb7/98thjjw1ZYQAAAABQy8oO1rq6ugb0VNvo97//fSZMmDAkRQHAWPTSIZ9dG7a8nyRN45tGrCYAAKByZQdrs2fPzje/+c383d/9XZKkUCikr68vn/vc53L00UcPeYEAMFY0L2ze4vlJn5804Lh4sQWBAABgNCg7WPvc5z6Xo446KnfddVfWr1+fCy+8MA899FCeeeaZ3H777cNRIwAAAADUnLKDtQMOOCD3339/lixZkvr6+nR1dWXOnDmZN29eJk+ePBw1AsCY0HlRZ/9+14au/p5qay5Yk6Zxhn8CAMBoU3awliRtbW1ZsGDBUNcCAGPa1uZOaxrXZF41AAAYherKveHrX/96/v3f/32z8//+7/+eb3zjG0NSFAAAAADUurKDtcsuuyx77bXXZucnTpyYSy+9dEiKAgAAAIBaV/ZQ0MceeyzTp0/f7Py0adPy+OOPD0lRADDWNY1vsvonAACMcmX3WJs4cWLuv//+zc7/v//v/5s999xzSIoCAAAAgFpXdrD2nve8Jx/5yEfys5/9LL29vent7c0tt9ySj370o3nPe94zHDUCAAAAQM0peyjoZz7zmTz22GN505velIaG0u19fX35i7/4C3OsAQCjRtf6rjQvbE6SdF7UaWVWAADKVnaPtfHjx+c73/lO/uu//iv/8i//kqVLl+a///u/83//7//N+PHjy3rWz3/+87z1rW/NlClTUigUcu211w64fsYZZ6RQKAzYDjvssAFt1q1bl3POOSd77bVXmpqa8ra3vS2//e1vy31bAAAAAFCWsnusbbT//vtn//3336EX7+rqysEHH5wPfOADecc73rHFNm9+85vz9a9/vf940/Du3HPPzfXXX59rrrkme+65Z84///ycdNJJufvuu1NfX79D9QEAAADA1gwqWJs/f37+7u/+Lk1NTZk/f/422y5atGjQL37iiSfmxBNP3GabCRMmpK2tbYvX2tvb87WvfS3f+ta3cuyxxyZJ/vmf/zlTp07NT37yk5xwwgmDrgUAGPu61ne9uL9hy/tJDAsFAGBQBhWs3XvvvdmwYUOS5J57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K8rJiWp2jrWVK1dm9erVOf744/vPTZgwIW984xvzi1/8Ikly9913Z8OGDQPaTJkyJTNmzOhvsyXr1q1LR0fHgA1gKHR3J9ddt+2ALCldX7as1L6ce5YuTX784+R3vxu6mpNST7VthWpJ6bqeawAAAC+q2WBt9erVSZJJkyYNOD9p0qT+a6tXr8748eOz++67b7XNlixcuDCtra3929SpU4e4emBn1dHx4pxq29PXV2pfzj3FYvLmNyf77JPssktywQWV1/pS//7vg2v3b/82NK8HAAAwFtRssLZRoVAYcFwsFjc7t6nttbnooovS3t7evz3xxBNDUitAS0tpTrLBqKsrtS/nnpdaty75h39IXv/68u99qUcfLQV2g9HXZ0EDAACAjWo2WGtra0uSzXqerV27tr8XW1tbW9avX59nn312q222ZMKECWlpaRmwAQyFxsbSPGgNDdtu19CQnHJKqf1g79mau+7asZ5r998/vO0BAADGqpoN1qZPn562trbcfPPN/efWr1+f2267LUcccUSS5HWve13GjRs3oM2qVavy4IMP9rcBGGnz5yfbW5i4tzc577zy7tmWf/qnyu896KDhbQ8AADBWVTVY6+zszH333Zf77rsvSWnBgvvuuy+PP/54CoVCzj333Fx66aVZtmxZHnzwwZxxxhnZdddd8973vjdJ0tramg9+8IM5//zz89Of/jT33ntv3ve+9+XAAw/MscceW8V3BuzMZs0qLQawLe95TzJz5sB7Fi9OCoXKeq5t2FD5ggb77lt63cGoqyu1BwAAoMrB2l133ZXXvva1ee1rX5skmT9/fl772tfm05/+dJLkwgsvzLnnnpu5c+fmkEMOye9+97vcdNNN2W233fqfccUVV+Ttb397Tj311MycOTO77rprrr/++tTX11flPQGsWJF85zvbbnPNNcnttw88d+aZyfLlpWGhgw26XurBB8u/Z6N3vWtw7U49tfLXAAAAGGsKxeJgp6weuzo6OtLa2pr29nbzrQE7bM6c5Prrk56erbdpaCgFaN/97pavn3xy8oMfDH610CS5997kNa8pq9QBpk1LHn9869df/vLksccqfz4AAMBoUE5OVLNzrAGMRt3dyXXXbTtUS0rXly0rtd/SM8oN1ZJS8LW92tas2fJrJqXQ7D3v2XyF0rq60nmhGgAAwECCNYBtWPnsyhQW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2N5wAAAAMJbVdLCWJK9+9auzatWq/u2BBx7ov/bZz342ixYtypVXXpk777wzbW1tOe644/Lcc89VsWJ2xKJFSX39ttvU1ydXXDEy9WyquztZs2Zszfm2xx7J5MmDaztlSqn9RtvrDQcAAABjWc0Haw0NDWlra+vf9t577ySl3mr/+I//mE9+8pOZM2dOZsyYkW984xt5/vnn8+1vf7vKVVOJ7u7kuus276m2qZ6eZNmykQ23VqwozS3W3Dw253z7m78Z2nYAAACwM6j5YO2RRx7JlClTMn369LznPe/J//zP/yRJVq5cmdWrV+f444/vbzthwoS88Y1vzC9+8YttPnPdunXp6OgYsFF9HR0vzqm2PX19pfYjYcmSZPbssT3n29y5yWmnbbvNaaclZ501MvUAAADAaFDTwdqhhx6ab37zm/nxj3+cr3zlK1m9enWOOOKIPP3001m9enWSZNKkSQPumTRpUv+1rVm4cGFaW1v7t6lTpw7be2DwWlpenAx/e+rqSu2H284059u3v11a0XPTOdemTCmd1xEUAAAABqrpYO3EE0/MO97xjhx44IE59thjc8MNNyRJvvGNb/S3KRQKA+4pFoubndvURRddlPb29v7tiSeeGPriKVtjY2llyYaGbbdraEhOOWVk5vWq9TnfhtpZZyW/+13y9NPJAw+U/v7ud3qqAQAAwJbUdLC2qaamphx44IF55JFH+lcH3bR32tq1azfrxbapCRMmpKWlZcBGbZg/P+nt3Xab3t7kvPOGv5ZanvNtuO2xRzJjxsCFCgAAAICBRlWwtm7duvz617/O5MmTM3369LS1teXmm2/uv75+/frcdtttOeKII6pYJTti1qzSsMNCYfOeaw0NpfOLFyczZw5/LbU65xsAAABQG2o6WLvgggty2223ZeXKlfmP//iPvPOd70xHR0dOP/30FAqFnHvuubn00kuzbNmyPPjggznjjDOy66675r3vfW+1S2cHnHlmsnx5aVjoxjnX6upKx8uXl66PhFqc8w0AAACoHduZzaq6fvvb3+a0007L73//++y999457LDDcscdd2TatGlJkgsvvDDd3d2ZO3dunn322Rx66KG56aabsttuu1W5cnbUzJmlrbu71BOspWVk5lR7qY1zvl1//baHgzY0lNqNdH0AAABAdRWKxWKx2kVUW0dHR1pbW9Pe3m6+NQZYsSKZPbu0+ufWFAqlnnQjMTwVAAAAGF7l5EQ1PRQUqq2W5nwDAAAAaotgDbajVuZ8AwAAAGpLTc+xBrWiFuZ8AwAAAGqLYA3K0NgoUAMAAABKDAUFAAAAgAoI1gAAAACgAoK1Maq7O1mzpvQXAAAAgKEnWBtjVqxI5sxJmpuTtrbS3zlzkttvr3ZlAAAAAGOLYG0MWbIkmT07uf76pK+vdK6vr3R85JHJVVdVtz4AAACAsUSwNkasWJHMm5cUi0lPz8BrPT2l83Pn6rkGAAAAMFQEa2PEokVJff2229TXJ1dcMTL1AAAAAIx1grUxoLs7ue66zXuqbaqnJ1m2zIIGAAAAAENBsDYGdHS8OKfa9vT1ldoDAAAAsGMEa2NAS0tSN8j/S9bVldoDAAAAsGMEa2NAY2Ny8slJQ8O22zU0JKecUmoPAAAAwI4RrI0R8+cnvb3bbtPbm5x33sjUAwAAADDWCdbGiFmzksWLk0Jh855rDQ2l84sXJzNnVqc+AAAAgLFGsDaGnHlmsnx5aVjoxjnX6upKx8uXl64DAAAAMDS2MysXo83MmaWtu7u0+mdLiznVAAAAAIaDYG2MamwUqAEAAAAMJ0NBAQAAAKACgjUAAAAAqIBgDQAAAAAqIFgDAAAAgAoI1gAAAACgAoI1AAAAAKiAYA0AAAAAKiBYAwAAAIAKCNYAAAAAoAKCNQAAAACogGANAAAAACogWAMAAACACgjWAAAAAKACgjUAAAAAqIBgDQAAAAAqIFgDAAAAgAoI1gAAAACgAoI1AAAAAKiAYA0AAAAAKiBYAwAAAIAKCNYAAAAAoAKCNQAAAACogGANAAAAACogWAMAAACACgjWAAAAAKACgjUAAAAAqEBDtQuoBcViMUnS0dFR5UoAAAAAqKaN+dDGvGhbBGtJnnvuuSTJ1KlTq1wJAAAAALXgueeeS2tr6zbbFIqDid/GuL6+vjz55JPZbbfdUigUql0ObKajoyNTp07NE088kZaWlmqXA8PGd52dge85OwvfdXYWvuvsDHa273mxWMxzzz2XKVOmpK5u27Oo6bGWpK6uLvvss0+1y4Dtamlp2Sl+xMB3nZ2B7zk7C991dha+6+wMdqbv+fZ6qm1k8QIAAAAAqIBgDQAAAAAqIFiDUWDChAm5+OKLM2HChGqXAsPKd52dge85OwvfdXYWvuvsDHzPt87iBQAAAABQAT3WAAAAAKACgjUAAAAAqIBgDQAAAAAqIFgDAAAAgAoI1mCE/PznP89b3/rWTJkyJYVCIddee+2A68ViMZdcckmmTJmSxsbGHHXUUXnooYcGtFm3bl3OOeec7LXXXmlqasrb3va2/Pa3vx3Q5tlnn8373//+tLa2prW1Ne9///vzhz/8YZjfHbxoe9/1M844I4VCYcB22GGHDWjju06tW7hwYV7/+tdnt912y8SJE/P2t789Dz/88IA2ftcZ7QbzPfebzliwZMmSHHTQQWlpaUlLS0sOP/zw/OhHP+q/7vecsWB733O/55UTrMEI6erqysEHH5wrr7xyi9c/+9nPZtGiRbnyyitz5513pq2tLccdd1yee+65/jbnnntuli1blmuuuSYrVqxIZ2dnTjrppPT29va3ee9735v77rsvN954Y2688cbcd999ef/73z/s7w822t53PUne/OY3Z9WqVf3bD3/4wwHXfdepdbfddlvmzZuXO+64IzfffHN6enpy/PHHp6urq7+N33VGu8F8zxO/6Yx+++yzTy677LLcddddueuuu3LMMcfk5JNP7g/P/J4zFmzve574Pa9YERhxSYrLli3rP+7r6yu2tbUVL7vssv5zL7zwQrG1tbV41VVXFYvFYvEPf/hDcdy4ccVrrrmmv83vfve7Yl1dXfHGG28sFovF4q9+9atikuIdd9zR3+aXv/xlMUnxv/7rv4b5XcHmNv2uF4vF4umnn148+eSTt3qP7zqj0dq1a4tJirfddluxWPS7zti06fe8WPSbzti1++67F7/61a/6PWdM2/g9Lxb9nu8IPdagBqxcuTKrV6/O8ccf339uwoQJeeMb35hf/OIXSZK77747GzZsGNBmypQpmTFjRn+bX/7yl2ltbc2hhx7a3+awww5La2trfxuoBbfeemsmTpyY/fffP3/1V3+VtWvX9l/zXWc0am9vT5LsscceSfyuMzZt+j3fyG86Y0lvb2+uueaadHV15fDDD/d7zpi06fd8I7/nlWmodgFAsnr16iTJpEmTBpyfNGlSHnvssf4248ePz+67775Zm433r169OhMnTtzs+RMnTuxvA9V24okn5l3velemTZuWlStX5lOf+lSOOeaY3H333ZkwYYLvOqNOsVjM/PnzM2vWrMyYMSOJ33XGni19zxO/6YwdDzzwQA4//PC88MILaW5uzrJly3LAAQf0hwF+zxkLtvY9T/ye7wjBGtSQQqEw4LhYLG52blObttlS+8E8B0bKu9/97v79GTNm5JBDDsm0adNyww03ZM6cOVu9z3edWnX22Wfn/vvvz4oVKza75nedsWJr33O/6YwVr3zlK3PfffflD3/4Q773ve/l9NNPz2233dZ/3e85Y8HWvucHHHCA3/MdYCgo1IC2trYk2SzFX7t2bf+/jrW1tWX9+vV59tlnt9lmzZo1mz3/qaee2uxf2aBWTJ48OdOmTcsjjzySxHed0eWcc87J97///fzsZz/LPvvs03/e7zpjyda+51viN53Ravz48dl3331zyCGHZOHChTn44IPzhS98we85Y8rWvudb4vd88ARrUAOmT5+etra23Hzzzf3n1q9fn9tuuy1HHHFEkuR1r3tdxo0bN6DNqlWr8uCDD/a3Ofzww9Pe3p7//M//7G/zH//xH2lvb+9vA7Xm6aefzhNPPJHJkycn8V1ndCgWizn77LOzdOnS3HLLLZk+ffqA637XGQu29z3fEr/pjBXFYjHr1q3ze86YtvF7viV+z8swokslwE7sueeeK957773Fe++9t5ikuGjRouK9995bfOyxx4rFYrF42WWXFVtbW4tLly4tPvDAA8XTTjutOHny5GJHR0f/M84888ziPvvsU/zJT35SvOeee4rHHHNM8eCDDy729PT0t3nzm99cPOigg4q//OUvi7/85S+LBx54YPGkk04a8ffLzmtb3/XnnnuueP755xd/8YtfFFeuXFn82c9+Vjz88MOLf/RHf+S7zqhy1v/f3v3HVFX/cRx/XRX15oWrIv5oIqgEgbUmYvlj+CNL3DWnQk0XFGRJ5FJpZSYzSrMfm/lrNSdrV0yzBTVpk9hICQVzWqJYKWIZzGqQRthE/AV8vn98v555QyCufvX7xedjO9v9fO7nfM77cz5n54/3Puec554zTqfT7Nq1y1RVVVlbfX291Yb7Ov7ftXWdc09HR7FkyRJTVFRkKioqzHfffWfS0tJMp06dzJdffmmM4X6OjqG165z7+fUhsQbcJIWFhUZSsy0xMdEYY0xTU5N57bXXTP/+/U23bt3MuHHjzPfff+/Rx/nz583zzz9vevfubex2u3nkkUfMyZMnPdrU1NSY+Ph44+vra3x9fU18fLypra29SaMEWr/W6+vrzeTJk01AQIDx8fExgwYNMomJic2uY651/K+71jUuyWRmZlptuK/j/11b1zn3dHQUc+bMMUFBQaZr164mICDATJo0yUqqGcP9HB1Da9c59/PrYzPGmJu3Pg4AAAAAAADoGHjHGgAAAAAAAOAFEmsAAAAAAACAF0isAQAAAAAAAF4gsQYAAAAAAAB4gcQaAAAAAAAA4AUSawAAAAAAAIAXSKwBAAAAAAAAXiCxBgAAAAAAAHiBxBoAAMANFBwcrLVr197qMAAAAHATkFgDAAAdks1ma3VLSkpqc//PP//8hsd17tw5LV68WEOGDFH37t0VEBCgCRMmKDc394Yf62aprKy85jlOSEi4Ycdo73wkJyerc+fO+uSTT25YDAAAAH/X5VYHAAAA8N9QVVVl/c7KylJ6errKy8utOrvdfivCUkpKir755hu9//77ioiIUE1Njfbu3auamppbEs/VLl26pK5du3q9/86dOzVs2DCrfKvOcX19vbKysrRo0SK53W7Nnj271fbXO24AAHD7YsUaAADokPr3729tTqdTNpvNo+7jjz/W0KFD1bVrV4WFhWnLli3WvsHBwZKkmTNnymazWeUTJ05o+vTp6tevnxwOh0aOHKmdO3e2K67t27crLS1NLpdLwcHBGjFihObPn6/ExESrzalTpzRt2jTZ7XYNHjxYW7du9XjE9MoKsdLSUmufM2fOyGazadeuXZKkxsZGPf300xo8eLDsdrvCwsK0bt06j1iSkpI0Y8YMvf3227rzzjsVGhoqSfrtt980a9Ys9erVS/7+/po+fboqKyvbHJu/v3+z8y5Jf/31l5KTk9W3b1/5+fnpwQcf1OHDh5udlxEjRqh79+4aMmSIli1bpoaGBkktz0dLPv30U0VERGjJkiX6+uuvm8Xu7bi//fZbPfzww+rTp4+cTqfGjx+vgwcPtnleAABAx0ViDQAA3HZycnK0cOFCvfjii/rhhx/07LPP6qmnnlJhYaGkfydQJCkzM1NVVVVWua6uTi6XSzt37tShQ4cUExOjadOm6eTJk//42P3791deXp7Onj3bYpukpCRVVlbqq6++0meffab169fr1KlT7RpjU1OTBg4cqOzsbB09elTp6elKS0tTdna2R7uCggKVlZVpx44dys3NVX19vSZOnCiHw6GioiLt2bNHDodDU6ZM0aVLl9oVgyQZYzR1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\n",
      "text/plain": [
       "<Figure size 1500x1000 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plot_scatter_chart(df8,\"Hebbal\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "79a58c32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Count')"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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q6+vT//+/bvcAAAAAAAAtkePh5hnq1ar6ezszLBhw9LY2Jg5c+bUtm3cuDFz587N0UcfnSQ58sgj07t37y4zK1asyJIlS2ozY8aMSXt7e+6///7azH333Zf29vbaDAAAAAAAQAm9evLFP/nJT2bixIlpbm7O2rVrM2vWrNxzzz1pbW1NXV1dpk+fnksuuSQHH3xwDj744FxyySV59atfnSlTpiRJKpVKzjrrrFx44YXZb7/9MnDgwFx00UUZOXJkxo4dmyQ59NBDM2HChEydOjXXXHNNkuTss8/OpEmTMnz48B47dgAAAAAAYPfXoyFm5cqVaWlpyYoVK1KpVHL44YentbU1J554YpLkYx/7WDZs2JCPfOQjWb16dUaNGpU77rgj/fr1q+3jqquuSq9evXLaaadlw4YNOeGEE3Lddddl7733rs3ceOONOf/88zNu3LgkyeTJkzNz5swde7AAAAAAAMAep65arVZ7ehG7go6OjlQqlbS3t/u9GOhGB33itp5eAt1k+WUn9fQSAAAAAGCHeandYKf7jRgAAAAAAIDdhRADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQiBADAAAAAABQSI+GmEsvvTRvfetb069fvzQ0NORd73pXHn300S4zZ555Zurq6rrcRo8e3WWms7Mz06ZNy6BBg9K3b99Mnjw5TzzxRJeZ1atXp6WlJZVKJZVKJS0tLVmzZk3pQwQAAAAAAPZgPRpi5s6dm3PPPTcLFy7MnDlz8swzz2TcuHFZv359l7kJEyZkxYoVtdvtt9/eZfv06dMze/bszJo1K/Pmzcu6desyadKkbN68uTYzZcqULF68OK2trWltbc3ixYvT0tKyQ44TAAAAAADYM/XqyRdvbW3tcv/aa69NQ0NDFi1alHe+8521x+vr69PY2Pic+2hvb8+3v/3t3HDDDRk7dmyS5Hvf+16am5tz5513Zvz48Vm6dGlaW1uzcOHCjBo1KknyzW9+M2PGjMmjjz6a4cOHFzpCAAAAAABgT7ZT/UZMe3t7kmTgwIFdHr/nnnvS0NCQQw45JFOnTs2qVatq2xYtWpRNmzZl3LhxtceampoyYsSIzJ8/P0myYMGCVCqVWoRJktGjR6dSqdRmnq2zszMdHR1dbgAAAAAAANtjpwkx1Wo1F1xwQd7+9rdnxIgRtccnTpyYG2+8MXfddVeuuOKKPPDAAzn++OPT2dmZJGlra0ufPn0yYMCALvsbPHhw2traajMNDQ3bvGZDQ0Nt5tkuvfTS2u/JVCqVNDc3d9ehAgAAAAAAe4ge/Wqyv3feeefloYceyrx587o8fvrpp9f+PWLEiBx11FEZOnRobrvttpx66qnPu79qtZq6urra/b//9/PN/L2LL744F1xwQe1+R0eHGAMAAAAAAGyXneKKmGnTpuUnP/lJ7r777hxwwAEvODtkyJAMHTo0jz32WJKksbExGzduzOrVq7vMrVq1KoMHD67NrFy5cpt9PfXUU7WZZ6uvr0///v273AAAAAAAALZHj4aYarWa8847L7fcckvuuuuuDBs27EWf8/TTT+fxxx/PkCFDkiRHHnlkevfunTlz5tRmVqxYkSVLluToo49OkowZMybt7e25//77azP33Xdf2tvbazMAAAAAAADdrUe/muzcc8/NTTfdlB//+Mfp169f7fdaKpVK9tlnn6xbty4zZszIe97zngwZMiTLly/PJz/5yQwaNCjvfve7a7NnnXVWLrzwwuy3334ZOHBgLrrooowcOTJjx45Nkhx66KGZMGFCpk6dmmuuuSZJcvbZZ2fSpEkZPnx4zxw8AAAAAACw2+vREHP11VcnSY499tguj1977bU588wzs/fee+fhhx/Od7/73axZsyZDhgzJcccdl5tvvjn9+vWrzV911VXp1atXTjvttGzYsCEnnHBCrrvuuuy99961mRtvvDHnn39+xo0blySZPHlyZs6cWf4gAQAAAACAPVZdtVqt9vQidgUdHR2pVCppb2/3ezHQjQ76xG09vQS6yfLLTurpJQAAAADADvNSu0GP/kYMAAAAAADA7kyIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKESIAQAAAAAAKKRXTy8AAF6ugz5xW08vgW6y/LKTenoJAAAAAEW4IgYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKCQHg0xl156ad761remX79+aWhoyLve9a48+uijXWaq1WpmzJiRpqam7LPPPjn22GPzyCOPdJnp7OzMtGnTMmjQoPTt2zeTJ0/OE0880WVm9erVaWlpSaVSSaVSSUtLS9asWVP6EAEAAAAAgD1Yj4aYuXPn5txzz83ChQszZ86cPPPMMxk3blzWr19fm7n88stz5ZVXZubMmXnggQfS2NiYE088MWvXrq3NTJ8+PbNnz86sWbMyb968rFu3LpMmTcrmzZtrM1OmTMnixYvT2tqa1tbWLF68OC0tLTv0eAEAAAAAgD1LXbVarfb0IrZ66qmn0tDQkLlz5+ad73xnqtVqmpqaMn369Hz84x9P8rerXwYPHpwvfvGLOeecc9Le3p79998/N9xwQ04//fQkyZNPPpnm5ubcfvvtGT9+fJYuXZrDDjssCxcuzKhRo5IkCxcuzJgxY/Kb3/wmw4cPf9G1dXR0pFKppL29Pf379y/3R4A9zEGfuK2nl0A3WX7ZSTv8Nb1/dh898f4BAAAAeCVeajfYqX4jpr29PUkycODAJMmyZcvS1taWcePG1Wbq6+tzzDHHZP78+UmSRYsWZdOmTV1mmpqaMmLEiNrMggULUqlUahEmSUaPHp1KpVKbebbOzs50dHR0uQEAAAAAAGyPnSbEVKvVXHDBBXn729+eESNGJEna2tqSJIMHD+4yO3jw4Nq2tra29OnTJwMGDHjBmYaGhm1es6GhoTbzbJdeemnt92QqlUqam5tf2QECAAAAAAB7nJ0mxJx33nl56KGH8v3vf3+bbXV1dV3uV6vVbR57tmfPPNf8C+3n4osvTnt7e+32+OOPv5TDAAAAAAAAqNkpQsy0adPyk5/8JHfffXcOOOCA2uONjY1Jss1VK6tWrapdJdPY2JiNGzdm9erVLzizcuXKbV73qaee2uZqm63q6+vTv3//LjcAAAAAAIDt0aMhplqt5rzzzsstt9ySu+66K8OGDeuyfdiwYWlsbMycOXNqj23cuDFz587N0UcfnSQ58sgj07t37y4zK1asyJIlS2ozY8aMSXt7e+6///7azH333Zf29vbaDAAAAAAAQHfr1ZMvfu655+amm27Kj3/84/Tr16925UulUsk+++yTurq6TJ8+PZdcckkOPvjgHHzwwbnkkkvy6le/OlOmTKnNnnXWWbnwwguz3377ZeDAgbnooosycuTIjB07Nkly6KGHZsKECZk6dWquueaaJMnZZ5+dSZMmZfjw4T1z8AAAAAAAwG6vR0PM1VdfnSQ59thjuzx+7bXX5swzz0ySfOxjH8uGDRvykY98JKtXr86oUaNyxx13pF+/frX5q666Kr169cppp52WDRs25IQTTsh1112XvffeuzZz44035vzzz8+4ceOSJJMnT87MmTPLHiAAAAAAALBHq6tWq9XtfdLrXve6PPDAA9lvv/26PL5mzZq85S1vye9///tuW+DOoqOjI5VKJe3t7X4vBrrRQZ+4raeXQDdZftlJO/w1vX92Hz3x/gEAAAB4JV5qN3hZvxGzfPnybN68eZvHOzs786c//enl7BIAAAAAAGC3s11fTfaTn/yk9u///u//TqVSqd3fvHlzfvrTn+aggw7qtsUBAAAAAADsyrYrxLzrXe9KktTV1eWMM87osq1379456KCDcsUVV3Tb4gAAAAAAAHZl2xVitmzZkiQZNmxYHnjggQwaNKjIogAAAAAAAHYH2xVitlq2bFl3rwMAAAAAAGC387JCTJL89Kc/zU9/+tOsWrWqdqXMVt/5znde8cIAAAAA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aW9vz/3331+bue+++9Le3l6bAShhR57HxowZkyVLlmTFihW1mTvuuCP19fU58sgjix4nsGd7+umn8/jjj2fIkCFJnNeAnUu1Ws15552XW265JXfddVeGDRvWZbvPa8Cu5sXOa89ll/q8VgWg21144YXVe+65p/r73/++unDhwuqkSZOq/fr1qy5fvrxarVarl112WbVSqVRvueWW6sMPP1x93/veVx0yZEi1o6Ojto8PfehD1QMOOKB65513Vn/xi19Ujz/++OoRRxxRfeaZZ2ozEyZMqB5++OHVBQsWVBcsWFAdOXJkddKkSTv8eIHdz9q1a6u//OUvq7/85S+rSapXXnll9Ze//GX1D3/4Q7Va3XHnsWeeeaY6YsSI6gknnFD9xS9+Ub3zzjurBxxwQPW8887bcX8MYLfwQue1tWvXVi+88MLq/Pnzq8uWLavefffd1TFjxlRf+9rXOq8BO6UPf/jD1UqlUr3nnnuqK1asqN3+8pe/1GZ8XgN2JS92XtvVP68JMQAFnH766dUhQ4ZUe/fuXW1qaqqeeuqp1UceeaS2fcuWLdXPfvaz1cbGxmp9fX31ne98Z/Xhhx/uso8NGzZUzzvvvOrAgQOr++yzT3XSpEnVP/7xj11mnn766er73//+ar9+/ar9+vWrvv/976+uXr16RxwisJu7++67q0m2uZ1xxhnVanXHnsf+8Ic/VE866aTqPvvsUx04cGD1vPPOq/71r38tefjAbuiFzmt/+ctfquPGjavuv//+1d69e1cPPPDA6hlnnLHNOct5DdhZPNf5LEn12muvrc34vAbsSl7svLarf16r+38HCQAAAAAAQDfzGzEAAAAAAACFCDEAAAAAAACFCDEAAAAAAACFCDEAAAAAAACFCDEAAAAAAACFCDEAAAAAAACFCDEAAAAAAACFCDEAAEC3OPbYYzN9+vSeXgYAAMBORYgBAAC6OPPMM1NXV5e6urr07t07r3vd63LRRRdl/fr1L/i8W265Jf/2b/9WbF333HNPbV11dXXZf//9M3HixPzqV7/q9tdatWpVzjnnnBx44IGpr69PY2Njxo8fnwULFnT7a+0oz/77bb39y7/8S7fsf/ny5amrq8vixYu7ZX8AALC76NXTCwAAAHY+EyZMyLXXXptNmzbl3nvvzQc/+MGsX78+V1999TazmzZtSu/evTNw4MAdsrZHH300/fv3zx//+Mecf/75mTBhQn7zm9+kUqls9742btyYPn36bPP4e97znmzatCnXX399Xve612XlypX56U9/mj//+c/dcQivyPOt+aXa+vfbat999+2OZQEAAM/DFTEAAMA2tl4F0tzcnClTpuT9739/br311iTJjBkz8qY3vSnf+c538rrXvS719fWpVqvbfDVZZ2dnPvaxj6W5uTn19fU5+OCD8+1vf7u2/de//nX+8R//Mfvuu28GDx6clpaW/O///u+Lrq2hoSGNjY1529veliuuuCJtbW1ZuHBhkmT+/Pl55zvfmX322SfNzc05//zzu1zJc9BBB+Xzn/98zjzzzFQqlUydOnWb/a9Zsybz5s3LF7/4xRx33HEZOnRo3va2t+Xiiy/OSSedVJt77LHH8s53vjOvetWrcthhh2XOnDmpq6ur/Z22XoGyZs2a2nMWL16curq6LF++PEny9NNP533ve18OOOCAvPrVr87IkSPz/e9/v8t6jj322Jx33nm54IILMmjQoJx44ond8vfbetsaYv70pz/l9NNPz4ABA7LffvvllFNOqa1zq2uvvTaHHnpoXvWqV+Uf/uEf8vWvf722bdiwYUmSN7/5zamrq8uxxx77omsBAIA9gRADAAC8qH322SebNm2q3f/d736XH/zgB/nRj370vF9F9c///M+ZNWtWvvrVr2bp0qX5xje+Ufuf/itWrMgxxxyTN73pTXnwwQfT2tqalStX5rTTTtvudSV/uyrn4Ycfzvjx43PqqafmoYceys0335x58+blvPPO6/KcL33pSxkxYkQWLVqUT3/609vsc999982+++6bW2+9NZ2dnc/5ulu2bMmpp56avffeOwsXLsw3vvGNfPzjH9+utSfJX//61xx55JH5z//8zyxZsiRnn312Wlpact9993WZu/7669OrV6/8/Oc/zzXXXNNtf7+t/vKXv+S4447Lvvvum5/97GeZN29e9t1330yYMCEbN25Mknzzm9/Mpz71qXzhC1/I0qVLc8kll+TTn/50rr/++iTJ/fffnyS58847s2LFitxyyy0vay0AALC78dVkAADAC7r//vtz00035YQTTqg9tnHjxtxwww3Zf//9n/M5v/3tb/ODH/wgc+bMydixY5Mkr3vd62rbr7766rzlLW/JJZdcUnvsO9/5Tpqbm/Pb3/42hxxyyIuu6+mnn87nPve59OvXL29729ty0UUXZcqUKbWrcg4++OB89atfzTHHHJOrr746r3rVq5Ikxx9/fC666KLn3W+vXr1y3XXXZerUqfnGN76Rt7zlLTnmmGPy3ve+N4cffniSv8WGpUuXZvny5TnggAOSJJdcckkmTpz4ouv+e6997Wu7rGXatGlpbW3ND3/4w4waNar2+Bve8IZcfvnltfuf+cxnXvbfb+t6t/rDH/6QH//4x9lrr73yrW99K3V1dUn+dvXLa17zmtxzzz0ZN25c/u3f/i1XXHFFTj311CR/uwLm17/+da655pqcccYZtffCfvvtl8bGxu36OwAAwO5MiAEAALbxn//5n9l3333zzDPPZNOmTTnllFPyta99rbZ96NChzxthkr99Bdfee++dY4455jm3L1q0KHffffdz/j7J//zP/7ykkLB+/focfPDB+eEPf5iGhoYsWrQov/vd73LjjTfWZqvVarZs2ZJly5bl0EMPTZIcddRRL3zw+dtvxJx00km59957s2DBgrS2tubyyy/Pt771rZx55plZunRpDjzwwC5RY8yYMS+632fbvHlzLrvsstx8883505/+lM7OznR2dqZv375d5p695lfy97v33nvTr1+/2v0BAwbU/nZ//3jytyt2/ud//idPPfVUHn/88Zx11lldvs7tmWeeeVm/zQMAAHsSIQYAANjGcccdl6uvvjq9e/dOU1NTevfu3WX7s0PBs239yrDns2XLlpx88sn54he/uM22IUOGvOBz77333vTv3z/7779/lx+d37JlS84555ycf/752zznwAMPfMlr3+pVr3pVTjzxxJx44on5zGc+kw9+8IP57Gc/mzPPPDPVanWb+a1Xkmy1115/+ybov5/9+693S5IrrrgiV111Vb785S9n5MiR6du3b6ZPn177OrDnW/Mr+fsNGzYsr3nNa7bZ35FHHtklYm21//77569//WuSv3092d9fqZMke++99wu+HgAA7OmEGAAAYBt9+/bNG97whpf9/JEjR2bLli2ZO3du7avJ/t5b3vKW/OhHP8pBBx2UXr227z9LniskbN3nI4888orW/UIOO+yw3HrrrbV///GPf8yTTz6ZpqamJMmCBQu6zG+9YmjFihUZMGBAkmzzezr33ntvTjnllPzTP/1Tkr8Fkccee6x29c7zeSV/v+fb380335yGhoYucWurSqWS1772tfn973+f97///c+5jz59+iT521U+AADA/2+vnl4AAACw+znooINyxhln5AMf+EBuvfXWLFu2LPfcc09+8IMfJEnOPffc/PnPf8773ve+3H///fn973+fO+64Ix/4wAde9v/I//jHP54FCxbk3HPPzeLFi/PYY4/lJz/5SaZNm7Zd+3n66adz/PHH53vf+14eeuihLFu2LD/84Q9z+eWX55RTTkmSjB07NsOHD88///M/51e/+lXuvffefOpTn+qynze84Q1pbm7OjBkz8tvf/ja33XZbrrjiim1m5syZk/nz52fp0qU555xz0tbW9qJr7O6/3/vf//4MGjQop5xySu69994sW7Ysc+fOzUc/+tE88cQTSZIZM2bk0ksvzVe+8pX89re/zcMPP5xrr702V155ZZKkoaEh++yzT1pbW7Ny5cq0t7dv9zoAAGB3JMQAAABFXH311fk//+f/5CMf+Uj+4R/+IVOnTs369euTJE1NTfn5z3+ezZs3Z/z48RkxYkQ++tGPplKp1L7Sa3sdfvjhmTt3bh577LG84x3vyJvf/OZ8+tOfftGv6nq2fffdN6NGjcpVV12Vd77znRkxYkQ+/elPZ+rUqZk5c2aSv33t2OzZs9PZ2Zm3ve1t+eAHP5gvfOELXfbTu3fvfP/7389vfvObHHHEEfniF7+Yz3/+811mPv3pT+ctb3lLxo8fn2OPPTaNjY1517ve9aJr7O6/36tf/er87Gc/y4EHHphTTz01hx56aD7wgQ9kw4YNtStkPvjBD+Zb3/pWrrvuuowcOTLHHHNMrrvuugwbNixJ0qtXr3z1q1/NNddck6amplq0AgCAPV1d9bm+3BgAAIDtVldXl9mzZ7+kmAIAAOwZXBEDAAAAAABQiBADAAAAAABQSK+eXgAAAMDuwjc/AwAAz+aKGAAAAAAAgEKEGAAAAAAAgEKEGAAAAAAAgEKEGAAAAAAAgEKEGAAAAAAAgEKEGAAAAAAAgEKEGAAAAAAAgEKEGAAAAAAAgEKEGAAAAAAAgEL+P8wPdtaKX/vXAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 2000x1000 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib\n",
    "matplotlib.rcParams[\"figure.figsize\"] = (20,10)\n",
    "plt.hist(df8.price_per_sqft,rwidth=0.8)\n",
    "plt.xlabel(\"Price Per Square Feet\")\n",
    "plt.ylabel(\"Count\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc116683",
   "metadata": {},
   "source": [
    "# Outlier Removal Using Bathrooms Feature"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "3a8771fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 4.,  3.,  2.,  5.,  8.,  1.,  6.,  7.,  9., 12., 16., 13.])"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df8.bath.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "44aae366",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Count')"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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+Ppe9t1aj8A28tiUE2s9AgAAAADATsUdMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIUIMQAAAAAAAIW8YULM5MmTU1dXl5aWluq2SqWSiRMnpqmpKV27ds2IESOyePHiNq/bsGFDzj///Oy1117p1q1bxo4dmyeeeKLNmtWrV6e5uTn19fWpr69Pc3Nznnnmme1wVgAAAAAAQHv2hggxCxYsyE033ZSDDjqozfarr74606ZNy/Tp07NgwYI0Njbm+OOPz9q1a6trWlpaMnPmzNx+++257777sm7duowZMyabNm2qrhk3blwWLVqUWbNmZdasWVm0aFGam5u32/kBAAAAAADtU81DzLp16/L+978/X/rSl7LnnntWt1cqlVx77bX52Mc+lne/+90ZPHhwvvrVr+Yvf/lLbrvttiRJa2trvvzlL+ezn/1sRo4cmUMPPTS33nprHnroofzwhz9MkixZsiSzZs3Kf/3Xf2XYsGEZNmxYvvSlL+U73/lOli5dWpNzBgAAAAAA2oeah5hzzz03J554YkaOHNlm+7Jly7Jy5cqMGjWquq1Lly455phjMnfu3CTJwoUL89xzz7VZ09TUlMGDB1fX3H///amvr8/QoUOra4488sjU19dX17yUDRs2ZM2aNW0eAAAAAAAAr0XHWr757bffngcffDALFizYYt/KlSuTJA0NDW22NzQ05Pe//311TefOndvcSfPCmhdev3LlyvTu3XuL4/fu3bu65qVMnjw5V1555Ws7IQAAAAAAgL9Rsztili9fngsuuCC33nprdt1115ddV1dX1+Z5pVLZYtuLvXjNS61/teNcfvnlaW1trT6WL1/+iu8JAAAAAADwYjULMQsXLsyqVaty2GGHpWPHjunYsWPmzJmTz3/+8+nYsWP1TpgX37WyatWq6r7GxsZs3Lgxq1evfsU1Tz311Bbv//TTT29xt83f6tKlS3r06NHmAQAAAAAA8FrULMQcd9xxeeihh7Jo0aLq4/DDD8/73//+LFq0KAcccEAaGxsze/bs6ms2btyYOXPmZPjw4UmSww47LJ06dWqzZsWKFXn44Yera4YNG5bW1tbMnz+/uuaBBx5Ia2trdQ0AAAAAAEAJNfuOmO7du2fw4MFttnXr1i29evWqbm9pacmkSZPSv3//9O/fP5MmTcpuu+2WcePGJUnq6+tzxhlnZMKECenVq1d69uyZiy66KEOGDMnIkSOTJAMHDswJJ5yQM888MzfeeGOS5KyzzsqYMWMyYMCA7XjGAAAAAABAe1OzEPP3uOSSS7J+/fqcc845Wb16dYYOHZq77ror3bt3r6655ppr0rFjx5xyyilZv359jjvuuMyYMSMdOnSorvna176W8ePHZ9SoUUmSsWPHZvr06dv9fAAAAAAAgPalrlKpVGo9xI5gzZo1qa+vT2trq++LeZG+l3231iOwjTw25cRajwAAAAAAsEP4e7tBzb4jBgAAAAAAYGcnxAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABQixAAAAAAAABRS0xBzww035KCDDkqPHj3So0ePDBs2LN///ver+yuVSiZOnJimpqZ07do1I0aMyOLFi9scY8OGDTn//POz1157pVu3bhk7dmyeeOKJNmtWr16d5ubm1NfXp76+Ps3NzXnmmWe2xykCAAAAAADtWE1DzL777pspU6bkZz/7WX72s5/ln//5n3PSSSdVY8vVV1+dadOmZfr06VmwYEEaGxtz/PHHZ+3atdVjtLS0ZObMmbn99ttz3333Zd26dRkzZkw2bdpUXTNu3LgsWrQos2bNyqxZs7Jo0aI0Nzdv9/MFAAAAAADal7pKpVKp9RB/q2fPnvnMZz6T008/PU1NTWlpacmll16a5K93vzQ0NGTq1Kk5++yz09ramr333ju33HJLTj311CTJk08+mT59+uR73/teRo8enSVLlmTQoEGZN29ehg4dmiSZN29ehg0blkceeSQDBgz4u+Zas2ZN6uvr09ramh49epQ5+R1U38u+W+sR2EYem3JirUcAAAAAANgh/L3d4A3zHTGbNm3K7bffnmeffTbDhg3LsmXLsnLlyowaNaq6pkuXLjnmmGMyd+7cJMnChQvz3HPPtVnT1NSUwYMHV9fcf//9qa+vr0aYJDnyyCNTX19fXfNSNmzYkDVr1rR5AAAAAAAAvBY1DzEPPfRQdt9993Tp0iUf/vCHM3PmzAwaNCgrV65MkjQ0NLRZ39DQUN23cuXKdO7cOXvuuecrrundu/cW79u7d+/qmpcyefLk6nfK1NfXp0+fPq/rPAEAAAAAgPan5iFmwIABWbRoUebNm5ePfOQjOe200/KrX/2qur+urq7N+kqlssW2F3vxmpda/2rHufzyy9Pa2lp9LF++/O89JQAAAAAAgCRvgBDTuXPnvPnNb87hhx+eyZMn5+CDD87nPve5NDY2JskWd62sWrWqepdMY2NjNm7cmNWrV7/imqeeemqL93366ae3uNvmb3Xp0iU9evRo8wAAAAAAAHgtah5iXqxSqWTDhg3p169fGhsbM3v27Oq+jRs3Zs6cORk+fHiS5LDDDkunTp3arFmxYkUefvjh6pphw4altbU18+fPr6554IEH0traWl0DAAAAAABQQsdavvm///u/5x3veEf69OmTtWvX5vbbb8+9996bWbNmpa6uLi0tLZk0aVL69++f/v37Z9KkSdltt90ybty4JEl9fX3OOOOMTJgwIb169UrPnj1z0UUXZciQIRk5cmSSZODAgTnhhBNy5pln5sYbb0ySnHXWWRkzZkwGDBhQs3MHAAAAAAB2fjUNMU899VSam5uzYsWK1NfX56CDDsqsWbNy/PHHJ0kuueSSrF+/Puecc05Wr16doUOH5q677kr37t2rx7jmmmvSsWPHnHLKKVm/fn2OO+64zJgxIx06dKiu+drXvpbx48dn1KhRSZKxY8dm+vTp2/dkAQAAAACAdqeuUqlUaj3EjmDNmjWpr69Pa2ur74t5kb6XfbfWI7CNPDblxFqPAAAA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IQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKAQIQYAAAAAAKCQjrUeAGjf+l723VqPwDby2JQTaz0CAAAAALzhuCMGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgECEGAAAAAACgkJqGmB//+Md517velaamptTV1eWOO+5os79SqWTixIlpampK165dM2LEiCxevLjNmg0bNuT888/PXnvtlW7dumXs2LF54okn2qxZvXp1mpubU19fn/r6+jQ3N+eZZ54pfHYAAAAAAEB7V9MQ8+yzz+bggw/O9OnTX3L/1VdfnWnTpmX69OlZsGBBGhsbc/zxx2ft2rXVNS0tLZk5c2Zuv/323HfffVm3bl3GjBmTTZs2VdeMGzcuixYtyqxZszJr1qwsWrQozc3Nxc8PAAAAAABo3zrW8s3f8Y535B3veMdL7qtUKrn22mvzsY99LO9+97uTJF/96lfT0NCQ2267LWeffXZaW1vz5S9/ObfccktGjhyZJLn11lvTp0+f/PCHP8zo0aOzZMmSzJo1K/PmzcvQoUOTJF/60pcybNiwLF26NAMGDNg+JwsAAAAAALQ7b9jviFm2bFlWrlyZUaNGVbd16dIlxxxzTObOnZskWbhwYZ577rk2a5qamjJ48ODqmvvvvz/19fXVCJMkRx55ZOrr66trAAAAAAAASqjpHTGvZOXKlUmShoaGNtsbGhry+9//vrqmc+fO2XPPPbdY88LrV65cmd69e29x/N69e1fXvJQNGzZkw4YN1edr1qzZuhMBAAAAAADarTfsHTEvqKura/O8Uqlsse3FXrzmpda/2nEmT56c+vr66qNPnz6vcXIAAAAAAKC9e8OGmMbGxiTZ4q6VVatWVe+SaWxszMaNG7N69epXXPPUU09tcfynn356i7tt/tbll1+e1tbW6mP58uWv63wAAAAAAID25w0bYvr165fGxsbMnj27um3jxo2ZM2dOhg8fniQ57LDD0qlTpzZrVqxYkYcffri6ZtiwYWltbc38+fOrax544IG0trZW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HHjggVm0aFFaWlrS1NSU0047rdbjwXZXV1fX5nmlUtliG+zMnnvuubz3ve/N5s2b84UvfKHW40BxCxcuzOc+97k8+OCDft7TrmzevDlJctJJJ+WjH/1okuSQQw7J3Llz88UvfjHHHHNMLcfbbtwRAzV2/vnn584778w999yTfffdt9bjwHaxcOHCrFq1Kocddlg6duyYjh07Zs6cOfn85z+fjh07ZtOmTbUeEYrZZ599MmjQoDbbBg4cmMcff7xGE8H2cfHFF+eyyy7Le9/73gwZMiTNzc356Ec/6s5I2p3GxsYk2eLul1WrVm1xlwzsrJ577rmccsopWbZsWWbPnu1uGNqFn/zkJ1m1alX222+/6u/Bv//97zNhwoT07du31uNBMXvttVc6duzY7n8PdkcM1EilUsn555+fmTNn5t57702/fv1qPRJsN8cdd1weeuihNts+9KEP5a1vfWsuvfTSdOjQoUaTQXlve9vbsnTp0jbbfv3rX2f//fev0USwffzlL3/JLru0/XdgHTp0qP4LOWgv+vXrl8bGxsyePTuHHnpokmTjxo2ZM2dOpk6dWuPpoLwXIsyjjz6ae+65J7169ar1SLBdNDc3b/H9qKNHj05zc3M+9KEP1WgqKK9z58454ogj2v3vwUIM1Mi5556b2267Ld/61rfSvXv36r+Iq6+vT9euXWs8HZTVvXv3Lb4PqVu3bunVq5fvSWKn99GPfjTDhw/PpEmTcsopp2T+/Pm56aabctNNN9V6NCjqXe96Vz796U9nv/32y4EHHpif//znmTZtWk4//fRajwbb3Lp16/Kb3/ym+nzZsmVZtGhRevbsmf322y8tLS2ZNGlS+vfvn/79+2fSpEnZbbfdMm7cuBpODdvGK13/TU1N+d//+3/nwQcfzHe+851s2rSp+rtwz54907lz51qNDdvEq/38f3F47NSpUxobGzNgwIDtPSpsU6927V988cU59dRTc/TRR+fYY4/NrFmz8u1vfzv33ntv7YbezuoqlUql1kNAe/Rynwf6la98JR/84Ae37zDwBjBixIgccsghufbaa2s9ChT3ne98J5dffnkeffTR9OvXLxdeeGHOPPPMWo8FRa1duzaf+MQnMnPmzKxatSpNTU153/vel//4j//wf7yx07n33ntz7LHHbrH9tNNOy4wZM1KpVHLllVfmxhtvzOrVqzN06NBcf/31/kEKO4VXuv4nTpz4sp8Gcc8992TEiBGFp4OyXu3n/4v17ds3LS0taWlpKT8cFPT3XPs333xzJk+enCeeeCIDBgzIlVdemZNOOmk7T1o7QgwAAAAAAEAhu7z6EgAAAAAAALaGEAMAAAAAAFCIEAMAAAAAAFCIEAMAAAAAAFCIEAMAAAAAAFCIEAMAAAAAAFCIEAMAAAAAAFCIEAMAANTcY489lrq6uixatKjWo1Q98sgjOfLII7PrrrvmkEMOeck1I0aMSEtLS5H3L3lsAABg+xFiAACAfPCDH0xdXV2mTJnSZvsdd9yRurq6Gk1VW1dccUW6deuWpUuX5u677y72Pvfee2/q6uryzDPPFHsPAACgdoQYAAAgSbLrrrtm6tSpWb16da1H2WY2bty41a/97W9/m6OOOir7779/evXqtQ2nKue5556r9QgAAMCLCDEAAECSZOTIkWlsbMzkyZNfds3EiRO3+Jiua6+9Nn379q0+/+AHP5iTTz45kyZNSkNDQ/bYY49ceeWVef7553PxxRenZ8+e2XfffXPzzTdvcfxHHnkkw4cPz6677poDDzww9957b5v9v/rVr/LOd74zu+++exoaGtLc3Jw//vGP1f0jRozIeeedlwsvvDB77bVXjj/++Jc8j82bN+eqq67Kvvvumy5duuSQQw7JrFmzqvvr6uqycOHCXHXVVamrq8vEiRNf9s/k+eefz3nnnZc99tgjvXr1ysc//vFUKpXq/ltvvTWHH354unfvnsbGxowbNy6rVq1K8tePZDv22GOTJHvuuWfq6urywQ9+sM2cl1xySXr27JnGxsYt5qirq8sXv/jFnHTSSenWrVs+9alPJUluuOGGvOlNb0rnzp0zYMCA3HLLLW1e9/jjj+ekk07K7rvvnh49euSUU07JU089Vd3/wt/zzTffnP322y+77757PvKRj2TTpk25+uqr09jYmN69e+fTn/50m+NOnDgx++23X7p06ZKmpqaMHz/+Zf/cAACgvRBiAACAJEmHDh0yadKkXHfddXniiSde17F+9KMf5cknn8yPf/zjTJs2LRMnTsyYMWOy55575oEHHsiHP/zhfPjDH87y5cvbvO7iiy/OhAkT8vOf/zzDhw/P2LFj86c//SlJsmLFihxzzDE55JBD8rOf/SyzZs3KU089lVNOOaXNMb761a+mY8eO+elPf5obb7zxJef73Oc+l89+9rP5z//8z/zyl7/M6NGjM3bs2Dz66KPV9zrwwAMzYcKErFixIhdddNHLnusL7/fAAw/k85//fK655pr813/9V3X/xo0b88lPfjK/+MUvcscdd2TZsmXV2NKnT5/8v//3/5IkS5cuzYoVK/K5z32uzbG7deuWBx54IFdffXWuuuqqzJ49u837X3HFFTnppJPy0EMP5fTTT8/MmTNzwQUXZMKECXn44Ydz9tln50Mf+lDuueeeJEmlUsnJJ5+cP//5z5kzZ05mz56d3/72tzn11FPbHPe3v/1tvv/972fWrFn5+te/nptvvjknnnhinnjiicyZMydTp07Nxz/+8cybNy9J8n//7//NNddckxtvvDGPPvpo7rjjjgwZMuRl/9wAAKDdqAAAAO3eaaedVjnppJMqlUqlcuSRR1ZOP/30SqVSqcycObPyt782XHHFFZWDDz64zWuvueaayv7779/mWPvvv39l06ZN1W0DBgyovP3tb68+f/755yvdunWrfP3rX69UKpXKsmXLKkkqU6ZMqa557rnnKvvuu29l6tSplUqlUvnEJz5RGTVqVJv3Xr58eSVJZenSpZVKpVI55phjKocccsirnm9TU1Pl05/+dJttRxxxROWcc86pPj/44IMrV1xxxSse55hjjqkMHDiwsnnz5uq2Sy+9tDJw4MCXfc38+fMrSSpr166tVCqVyj333FNJUlm9evUWxz7qqKO2mPHSSy+tPk9SaWlpabNm+PDhlTPPPLPNtve85z2Vd77znZVKpVK56667Kh06dKg8/vjj1f2LFy+uJKnMnz+/Uqn89e95t912q6xZs6a6ZvTo0ZW+fftu8fc6efLkSqVSqXz2s5+tvOUtb6ls3LjxZc8dAADaI3fEAAAAbUydOjVf/epX86tf/Wqrj3HggQdml13+/183Ghoa2twd0aFDh/Tq1av6EV0vGDZsWPW/O3bsmMMPPzxLlixJkixcuDD33HNPdt999+rjrW99a5K/3r3xgsMPP/wVZ1uzZk2efPLJvO1tb2uz/W1ve1v1vV6LI488MnV1dW3O4dFHH82mTZuSJD//+c9z0kknZf/990/37t0zYsSIJH/9eLBXc9BBB7V5vs8++2zxZ/bi812yZMkrntuSJUvSp0+f9OnTp7p/0KBB2WOPPdqcf9++fdO9e/fq84aGhgwaNGiLv9cX5nnPe96T9evX54ADDsiZZ56ZmTNn5vnnn3/VcwQAgJ2dEAMAALRx9NFHZ/To0fn3f//3Lfbtsssubb7/JHnpL4jv1KlTm+d1dXUvuW3z5s2vOs8LkWPz5s1517velUWLFrV5PProozn66KOr67t16/aqx/zb476gUqlsse31evbZZzNq1KjsvvvuufXWW7NgwYLMnDkzyV8/suzV/D1/Zi91vq90bi93ni/e/lr/Dvv06ZOlS5fm+uuvT9euXXPOOefk6KOPfsnrAwAA2hMhBgAA2MKUKVPy7W9/O3Pnzm2zfe+9987KlSvbxJhFixZts/d94ftGkuT555/PwoULq3e9/OM//mMWL16cvn375s1vfnObx98bX5KkR48eaWpqyn333ddm+9y5czNw4MDXNfMLz/v3758OHTrkkUceyR//+MdMmTIlb3/72/PWt751iztaOnfunCTVO2her4EDB77iuQ0aNCiPP/54m+/n+dWvfpXW1tatOv+/1bVr14wdOzaf//znc++99+b+++/PQw899LqOCQAAOzohBgAA2MKQIUPy/ve/P9ddd12b7SNGjMjTTz+dq6++Or/97W9z/fXX5/vf//42e9/rr78+M2fOzCOPPJJzzz03q1evzumnn54kOffcc/PnP/8573vf+zJ//vz87ne/y1133ZXTTz/9NUeMiy++OFOnTs03vvGNLF26NJdddlkWLVqUCy644DXPvHz58lx44YVZunRpvv71r+e6666rHme//fZL586dc9111+V3v/td7rzzznzyk59s8/r9998/dXV1+c53vpOnn34669ate80zvPjcZsyYkS9+8Yt59NFHM23atHzzm9/MRRddlCQZOXJkDjrooLz//e/Pgw8+mPnz5+cDH/hAjjnmmFf9WLdXMmPGjHz5y1/Oww8/nN/97ne55ZZb0rVr1+y///6v63wAAGBHJ8QAAAAv6ZOf/OQWH0M2cODAfOELX8j111+fgw8+OPPnz6/+H/zbwpQpUzJ16tQcfPDB+clPfpJvfetb2WuvvZIkTU1N+elPf5pNmzZl9OjRGTx4cC644ILU19e3+d6Sv8f48eMzYcKETJgwIUOGDMmsWbNy5513pn///q955g984ANZv359/umf/innnntuzj///Jx11llJ/noH0YwZM/J//s//yaBBgzJlypT853/+Z5vX/8M//EOuvPLKXHbZZWloaMh55533mmf4WyeffHI+97nP5TOf+UwOPPDA3HjjjfnKV75S/W6aurq63HHHHdlzzz1z9NFHZ+TIkTnggAPyjW9843W97x577JEvfelLedvb3paDDjood999d7797W+nV69er+u4AACwo6urvPg3KwAAAAAAALYJd8QAAAAAAAAUIsQAAAAAAAAUIsQAAAAAAAAUIsQAAAAAAAAUIsQAAAAAAAAUIsQAAAAAAAAUIsQAAAAAAAAUIsQAAAAAAAAUIsQAAAAAAAAUIsQAAAAAAAAUIsQAAAAAAAAUIsQAAAAAAAAU8v8Ble8P7XG8bjQAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 2000x1000 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(df8.bath,rwidth=0.8)\n",
    "plt.xlabel(\"Number of bathrooms\")\n",
    "plt.ylabel(\"Count\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "44cff8e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "      <th>price_per_sqft</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5277</th>\n",
       "      <td>Neeladri Nagar</td>\n",
       "      <td>10 BHK</td>\n",
       "      <td>4000.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>160.0</td>\n",
       "      <td>10</td>\n",
       "      <td>4000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8486</th>\n",
       "      <td>other</td>\n",
       "      <td>10 BHK</td>\n",
       "      <td>12000.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>525.0</td>\n",
       "      <td>10</td>\n",
       "      <td>4375.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8575</th>\n",
       "      <td>other</td>\n",
       "      <td>16 BHK</td>\n",
       "      <td>10000.0</td>\n",
       "      <td>16.0</td>\n",
       "      <td>550.0</td>\n",
       "      <td>16</td>\n",
       "      <td>5500.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9308</th>\n",
       "      <td>other</td>\n",
       "      <td>11 BHK</td>\n",
       "      <td>6000.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>11</td>\n",
       "      <td>2500.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9639</th>\n",
       "      <td>other</td>\n",
       "      <td>13 BHK</td>\n",
       "      <td>5425.0</td>\n",
       "      <td>13.0</td>\n",
       "      <td>275.0</td>\n",
       "      <td>13</td>\n",
       "      <td>5069.124424</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            location    size  total_sqft  bath  price  bhk  price_per_sqft\n",
       "5277  Neeladri Nagar  10 BHK      4000.0  12.0  160.0   10     4000.000000\n",
       "8486           other  10 BHK     12000.0  12.0  525.0   10     4375.000000\n",
       "8575           other  16 BHK     10000.0  16.0  550.0   16     5500.000000\n",
       "9308           other  11 BHK      6000.0  12.0  150.0   11     2500.000000\n",
       "9639           other  13 BHK      5425.0  13.0  275.0   13     5069.124424"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df8[df8.bath>10]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1813d3f2",
   "metadata": {},
   "source": [
    "It is unusual to have 2 more bathrooms than number of bedrooms in a home"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "94b87c50",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "      <th>price_per_sqft</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1626</th>\n",
       "      <td>Chikkabanavar</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>2460.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>80.0</td>\n",
       "      <td>4</td>\n",
       "      <td>3252.032520</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5238</th>\n",
       "      <td>Nagasandra</td>\n",
       "      <td>4 Bedroom</td>\n",
       "      <td>7000.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>450.0</td>\n",
       "      <td>4</td>\n",
       "      <td>6428.571429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6711</th>\n",
       "      <td>Thanisandra</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1806.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>116.0</td>\n",
       "      <td>3</td>\n",
       "      <td>6423.034330</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8411</th>\n",
       "      <td>other</td>\n",
       "      <td>6 BHK</td>\n",
       "      <td>11338.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>1000.0</td>\n",
       "      <td>6</td>\n",
       "      <td>8819.897689</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           location       size  total_sqft  bath   price  bhk  price_per_sqft\n",
       "1626  Chikkabanavar  4 Bedroom      2460.0   7.0    80.0    4     3252.032520\n",
       "5238     Nagasandra  4 Bedroom      7000.0   8.0   450.0    4     6428.571429\n",
       "6711    Thanisandra      3 BHK      1806.0   6.0   116.0    3     6423.034330\n",
       "8411          other      6 BHK     11338.0   9.0  1000.0    6     8819.897689"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df8[df8.bath>df8.bhk+2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "64d5adfd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7251, 7)"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df9 = df8[df8.bath<df8.bhk+2]\n",
    "df9.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "1f64839e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>size</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "      <th>price_per_sqft</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1st Block Jayanagar</td>\n",
       "      <td>4 BHK</td>\n",
       "      <td>2850.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>428.0</td>\n",
       "      <td>4</td>\n",
       "      <td>15017.543860</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1st Block Jayanagar</td>\n",
       "      <td>3 BHK</td>\n",
       "      <td>1630.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>194.0</td>\n",
       "      <td>3</td>\n",
       "      <td>11901.840491</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              location   size  total_sqft  bath  price  bhk  price_per_sqft\n",
       "0  1st Block Jayanagar  4 BHK      2850.0   4.0  428.0    4    15017.543860\n",
       "1  1st Block Jayanagar  3 BHK      1630.0   3.0  194.0    3    11901.840491"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df9.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "309e2f96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1st Block Jayanagar</td>\n",
       "      <td>2850.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>428.0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1st Block Jayanagar</td>\n",
       "      <td>1630.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>194.0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1st Block Jayanagar</td>\n",
       "      <td>1875.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>235.0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              location  total_sqft  bath  price  bhk\n",
       "0  1st Block Jayanagar      2850.0   4.0  428.0    4\n",
       "1  1st Block Jayanagar      1630.0   3.0  194.0    3\n",
       "2  1st Block Jayanagar      1875.0   2.0  235.0    3"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df10 = df9.drop(['size','price_per_sqft'],axis='columns')\n",
    "df10.head(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1ae84eb",
   "metadata": {},
   "source": [
    "# USE ONE HOT ENCODING FOR LOCATION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "a8d6c1ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>1st Block Jayanagar</th>\n",
       "      <th>1st Phase JP Nagar</th>\n",
       "      <th>2nd Phase Judicial Layout</th>\n",
       "      <th>2nd Stage Nagarbhavi</th>\n",
       "      <th>5th Block Hbr Layout</th>\n",
       "      <th>5th Phase JP Nagar</th>\n",
       "      <th>6th Phase JP Nagar</th>\n",
       "      <th>7th Phase JP Nagar</th>\n",
       "      <th>8th Phase JP Nagar</th>\n",
       "      <th>9th Phase JP Nagar</th>\n",
       "      <th>...</th>\n",
       "      <th>Vishveshwarya Layout</th>\n",
       "      <th>Vishwapriya Layout</th>\n",
       "      <th>Vittasandra</th>\n",
       "      <th>Whitefield</th>\n",
       "      <th>Yelachenahalli</th>\n",
       "      <th>Yelahanka</th>\n",
       "      <th>Yelahanka New Town</th>\n",
       "      <th>Yelenahalli</th>\n",
       "      <th>Yeshwanthpur</th>\n",
       "      <th>other</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 242 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   1st Block Jayanagar  1st Phase JP Nagar  2nd Phase Judicial Layout  \\\n",
       "0                    1                   0                          0   \n",
       "1                    1                   0                          0   \n",
       "2                    1                   0                          0   \n",
       "\n",
       "   2nd Stage Nagarbhavi  5th Block Hbr Layout  5th Phase JP Nagar  \\\n",
       "0                     0                     0                   0   \n",
       "1                     0                     0                   0   \n",
       "2                     0                     0                   0   \n",
       "\n",
       "   6th Phase JP Nagar  7th Phase JP Nagar  8th Phase JP Nagar  \\\n",
       "0                   0                   0                   0   \n",
       "1                   0                   0                   0   \n",
       "2                   0                   0                   0   \n",
       "\n",
       "   9th Phase JP Nagar  ...  Vishveshwarya Layout  Vishwapriya Layout  \\\n",
       "0                   0  ...                     0                   0   \n",
       "1                   0  ...                     0                   0   \n",
       "2                   0  ...                     0                   0   \n",
       "\n",
       "   Vittasandra  Whitefield  Yelachenahalli  Yelahanka  Yelahanka New Town  \\\n",
       "0            0           0               0          0                   0   \n",
       "1            0           0               0          0                   0   \n",
       "2            0           0               0          0                   0   \n",
       "\n",
       "   Yelenahalli  Yeshwanthpur  other  \n",
       "0            0             0      0  \n",
       "1            0             0      0  \n",
       "2            0             0      0  \n",
       "\n",
       "[3 rows x 242 columns]"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#categorical infomation into numeric data we use pandas dummmies\n",
    "dummies = pd.get_dummies(df10.location)\n",
    "dummies.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "624ce9bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>location</th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "      <th>1st Block Jayanagar</th>\n",
       "      <th>1st Phase JP Nagar</th>\n",
       "      <th>2nd Phase Judicial Layout</th>\n",
       "      <th>2nd Stage Nagarbhavi</th>\n",
       "      <th>5th Block Hbr Layout</th>\n",
       "      <th>...</th>\n",
       "      <th>Vijayanagar</th>\n",
       "      <th>Vishveshwarya Layout</th>\n",
       "      <th>Vishwapriya Layout</th>\n",
       "      <th>Vittasandra</th>\n",
       "      <th>Whitefield</th>\n",
       "      <th>Yelachenahalli</th>\n",
       "      <th>Yelahanka</th>\n",
       "      <th>Yelahanka New Town</th>\n",
       "      <th>Yelenahalli</th>\n",
       "      <th>Yeshwanthpur</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1st Block Jayanagar</td>\n",
       "      <td>2850.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>428.0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1st Block Jayanagar</td>\n",
       "      <td>1630.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>194.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1st Block Jayanagar</td>\n",
       "      <td>1875.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>235.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1st Block Jayanagar</td>\n",
       "      <td>1200.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>130.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1st Block Jayanagar</td>\n",
       "      <td>1235.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>148.0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 246 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              location  total_sqft  bath  price  bhk  1st Block Jayanagar  \\\n",
       "0  1st Block Jayanagar      2850.0   4.0  428.0    4                    1   \n",
       "1  1st Block Jayanagar      1630.0   3.0  194.0    3                    1   \n",
       "2  1st Block Jayanagar      1875.0   2.0  235.0    3                    1   \n",
       "3  1st Block Jayanagar      1200.0   2.0  130.0    3                    1   \n",
       "4  1st Block Jayanagar      1235.0   2.0  148.0    2                    1   \n",
       "\n",
       "   1st Phase JP Nagar  2nd Phase Judicial Layout  2nd Stage Nagarbhavi  \\\n",
       "0                   0                          0                     0   \n",
       "1                   0                          0                     0   \n",
       "2                   0                          0                     0   \n",
       "3                   0                          0                     0   \n",
       "4                   0                          0                     0   \n",
       "\n",
       "   5th Block Hbr Layout  ...  Vijayanagar  Vishveshwarya Layout  \\\n",
       "0                     0  ...            0                     0   \n",
       "1                     0  ...            0                     0   \n",
       "2                     0  ...            0                     0   \n",
       "3                     0  ...            0                     0   \n",
       "4                     0  ...            0                     0   \n",
       "\n",
       "   Vishwapriya Layout  Vittasandra  Whitefield  Yelachenahalli  Yelahanka  \\\n",
       "0                   0            0           0               0          0   \n",
       "1                   0            0           0               0          0   \n",
       "2                   0            0           0               0          0   \n",
       "3                   0            0           0               0          0   \n",
       "4                   0            0           0               0          0   \n",
       "\n",
       "   Yelahanka New Town  Yelenahalli  Yeshwanthpur  \n",
       "0                   0            0             0  \n",
       "1                   0            0             0  \n",
       "2                   0            0             0  \n",
       "3                   0            0             0  \n",
       "4                   0            0             0  \n",
       "\n",
       "[5 rows x 246 columns]"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df11 = pd.concat([df10,dummies.drop('other',axis='columns')],axis='columns')\n",
    "df11.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "dcc30b87",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>price</th>\n",
       "      <th>bhk</th>\n",
       "      <th>1st Block Jayanagar</th>\n",
       "      <th>1st Phase JP Nagar</th>\n",
       "      <th>2nd Phase Judicial Layout</th>\n",
       "      <th>2nd Stage Nagarbhavi</th>\n",
       "      <th>5th Block Hbr Layout</th>\n",
       "      <th>5th Phase JP Nagar</th>\n",
       "      <th>...</th>\n",
       "      <th>Vijayanagar</th>\n",
       "      <th>Vishveshwarya Layout</th>\n",
       "      <th>Vishwapriya Layout</th>\n",
       "      <th>Vittasandra</th>\n",
       "      <th>Whitefield</th>\n",
       "      <th>Yelachenahalli</th>\n",
       "      <th>Yelahanka</th>\n",
       "      <th>Yelahanka New Town</th>\n",
       "      <th>Yelenahalli</th>\n",
       "      <th>Yeshwanthpur</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2850.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>428.0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1630.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>194.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2 rows × 245 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   total_sqft  bath  price  bhk  1st Block Jayanagar  1st Phase JP Nagar  \\\n",
       "0      2850.0   4.0  428.0    4                    1                   0   \n",
       "1      1630.0   3.0  194.0    3                    1                   0   \n",
       "\n",
       "   2nd Phase Judicial Layout  2nd Stage Nagarbhavi  5th Block Hbr Layout  \\\n",
       "0                          0                     0                     0   \n",
       "1                          0                     0                     0   \n",
       "\n",
       "   5th Phase JP Nagar  ...  Vijayanagar  Vishveshwarya Layout  \\\n",
       "0                   0  ...            0                     0   \n",
       "1                   0  ...            0                     0   \n",
       "\n",
       "   Vishwapriya Layout  Vittasandra  Whitefield  Yelachenahalli  Yelahanka  \\\n",
       "0                   0            0           0               0          0   \n",
       "1                   0            0           0               0          0   \n",
       "\n",
       "   Yelahanka New Town  Yelenahalli  Yeshwanthpur  \n",
       "0                   0            0             0  \n",
       "1                   0            0             0  \n",
       "\n",
       "[2 rows x 245 columns]"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df12 = df11.drop('location',axis='columns')\n",
    "df12.head(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9f85e1dc",
   "metadata": {},
   "source": [
    "# BUILD MODELL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "812f6680",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7251, 245)"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df12.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "2427b5e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>total_sqft</th>\n",
       "      <th>bath</th>\n",
       "      <th>bhk</th>\n",
       "      <th>1st Block Jayanagar</th>\n",
       "      <th>1st Phase JP Nagar</th>\n",
       "      <th>2nd Phase Judicial Layout</th>\n",
       "      <th>2nd Stage Nagarbhavi</th>\n",
       "      <th>5th Block Hbr Layout</th>\n",
       "      <th>5th Phase JP Nagar</th>\n",
       "      <th>6th Phase JP Nagar</th>\n",
       "      <th>...</th>\n",
       "      <th>Vijayanagar</th>\n",
       "      <th>Vishveshwarya Layout</th>\n",
       "      <th>Vishwapriya Layout</th>\n",
       "      <th>Vittasandra</th>\n",
       "      <th>Whitefield</th>\n",
       "      <th>Yelachenahalli</th>\n",
       "      <th>Yelahanka</th>\n",
       "      <th>Yelahanka New Town</th>\n",
       "      <th>Yelenahalli</th>\n",
       "      <th>Yeshwanthpur</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2850.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1630.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1875.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 244 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   total_sqft  bath  bhk  1st Block Jayanagar  1st Phase JP Nagar  \\\n",
       "0      2850.0   4.0    4                    1                   0   \n",
       "1      1630.0   3.0    3                    1                   0   \n",
       "2      1875.0   2.0    3                    1                   0   \n",
       "\n",
       "   2nd Phase Judicial Layout  2nd Stage Nagarbhavi  5th Block Hbr Layout  \\\n",
       "0                          0                     0                     0   \n",
       "1                          0                     0                     0   \n",
       "2                          0                     0                     0   \n",
       "\n",
       "   5th Phase JP Nagar  6th Phase JP Nagar  ...  Vijayanagar  \\\n",
       "0                   0                   0  ...            0   \n",
       "1                   0                   0  ...            0   \n",
       "2                   0                   0  ...            0   \n",
       "\n",
       "   Vishveshwarya Layout  Vishwapriya Layout  Vittasandra  Whitefield  \\\n",
       "0                     0                   0            0           0   \n",
       "1                     0                   0            0           0   \n",
       "2                     0                   0            0           0   \n",
       "\n",
       "   Yelachenahalli  Yelahanka  Yelahanka New Town  Yelenahalli  Yeshwanthpur  \n",
       "0               0          0                   0            0             0  \n",
       "1               0          0                   0            0             0  \n",
       "2               0          0                   0            0             0  \n",
       "\n",
       "[3 rows x 244 columns]"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = df12.drop(['price'],axis='columns')\n",
    "X.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "3993fc1f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7251, 244)"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "42d7f4eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    428.0\n",
       "1    194.0\n",
       "2    235.0\n",
       "Name: price, dtype: float64"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = df12.price\n",
    "y.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "600adc84",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7251"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "22817819",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "caada230",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8452277697874324"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "lr_clf = LinearRegression()\n",
    "lr_clf.fit(X_train,y_train)\n",
    "lr_clf.score(X_test,y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d104783",
   "metadata": {},
   "source": [
    "# Use K Fold cross validation to measure accuracy of our LinearRegression model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "c44eac2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.82430186, 0.77166234, 0.85089567, 0.80837764, 0.83653286])"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.model_selection import ShuffleSplit\n",
    "from sklearn.model_selection import cross_val_score\n",
    "\n",
    "cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)\n",
    "\n",
    "cross_val_score(LinearRegression(), X, y, cv=cv)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3346f0d6",
   "metadata": {},
   "source": [
    "We can see that in 5 iterations we get a score above 80% all the time. This is pretty good but we want to test few other algorithms for regression to see if we can get even better score. We will use GridSearchCV for this purpose"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c7c65887",
   "metadata": {},
   "source": [
    "# Find best model using GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "7828bf3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>model</th>\n",
       "      <th>best_score</th>\n",
       "      <th>best_params</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>linear_regression</td>\n",
       "      <td>0.818354</td>\n",
       "      <td>{}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>lasso</td>\n",
       "      <td>0.687429</td>\n",
       "      <td>{'alpha': 1, 'selection': 'cyclic'}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>decision_tree</td>\n",
       "      <td>0.754626</td>\n",
       "      <td>{'criterion': 'squared_error', 'splitter': 'ra...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               model  best_score  \\\n",
       "0  linear_regression    0.818354   \n",
       "1              lasso    0.687429   \n",
       "2      decision_tree    0.754626   \n",
       "\n",
       "                                         best_params  \n",
       "0                                                 {}  \n",
       "1                {'alpha': 1, 'selection': 'cyclic'}  \n",
       "2  {'criterion': 'squared_error', 'splitter': 'ra...  "
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def find_best_model_using_gridsearchcv(X, y):\n",
    "    algos = {\n",
    "        'linear_regression': {\n",
    "            'model': LinearRegression(),\n",
    "            'params': {\n",
    "                # 'normalize': [True, False] # This parameter is deprecated and removed\n",
    "            }\n",
    "        },\n",
    "        'lasso': {\n",
    "            'model': Lasso(),\n",
    "            'params': {\n",
    "                'alpha': [1, 2],\n",
    "                'selection': ['random', 'cyclic']\n",
    "            }\n",
    "        },\n",
    "        'decision_tree': {\n",
    "            'model': DecisionTreeRegressor(),\n",
    "            'params': {\n",
    "                'criterion': ['squared_error', 'friedman_mse'],\n",
    "                'splitter': ['best', 'random']\n",
    "            }\n",
    "        }\n",
    "    }\n",
    "    scores = []\n",
    "    cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)\n",
    "    for algo_name, config in algos.items():\n",
    "        gs = GridSearchCV(config['model'], config['params'], cv=cv, return_train_score=False)\n",
    "        gs.fit(X, y)\n",
    "        scores.append({\n",
    "            'model': algo_name,\n",
    "            'best_score': gs.best_score_,\n",
    "            'best_params': gs.best_params_\n",
    "        })\n",
    "\n",
    "    return pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])\n",
    "find_best_model_using_gridsearchcv(X,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a57f030b",
   "metadata": {},
   "source": [
    "# Test the model for few properties"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "db088edc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def predict_price(location,sqft,bath,bhk):    \n",
    "    loc_index = np.where(X.columns==location)[0][0]\n",
    "\n",
    "    x = np.zeros(len(X.columns))\n",
    "    x[0] = sqft\n",
    "    x[1] = bath\n",
    "    x[2] = bhk\n",
    "    if loc_index >= 0:\n",
    "        x[loc_index] = 1\n",
    "\n",
    "    return lr_clf.predict([x])[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "e53f3f12",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HP\\anaconda3\\lib\\site-packages\\sklearn\\base.py:420: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "83.49904677185246"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "predict_price('1st Phase JP Nagar',1000, 2, 2) # location, 1000sqft , 2bathroom,2bedroom"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "1104ae9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HP\\anaconda3\\lib\\site-packages\\sklearn\\base.py:420: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "86.80519395211893"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "predict_price('1st Phase JP Nagar',1000, 3, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "f6e51f6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HP\\anaconda3\\lib\\site-packages\\sklearn\\base.py:420: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "181.2781548400676"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "predict_price('Indira Nagar',1000, 2, 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ace67278",
   "metadata": {},
   "source": [
    "# Export the tested model to a pickle file\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "9492ac06",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "with open('banglore_home_prices_model.pickle','wb') as f:\n",
    "    pickle.dump(lr_clf,f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "6e17946d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "columns = {\n",
    "    'data_columns' : [col.lower() for col in X.columns]\n",
    "}\n",
    "with open(\"columns.json\",\"w\") as f:\n",
    "    f.write(json.dumps(columns))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5484163",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
