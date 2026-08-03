# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_10:40:54_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-08-03 10:40:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-03 10:40:54 UTC

- **168,392** saved flights
- **55,003** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **168,392** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **2,030,852.7 tonnes** estimated CO2 emissions
- **117,730,591 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6716 |
| 2 | SkyWest Airlines | 6146 |
| 3 | EJA | 3348 |
| 4 | IndiGo | 2972 |
| 5 | American Airlines | 2657 |
| 6 | Southwest Airlines | 2650 |
| 7 | ENY | 2099 |
| 8 | Delta Air Lines | 2009 |
| 9 | LATAM Airlines | 1560 |
| 10 | Lufthansa | 1549 |
| 11 | AZU | 1482 |
| 12 | WIF | 1407 |
| 13 | Vueling | 1387 |
| 14 | LXJ | 1318 |
| 15 | AXM | 1166 |
| 16 | Swiss International | 1153 |
| 17 | easyJet | 1135 |
| 18 | EJU | 1036 |
| 19 | Alaska Airlines | 1031 |
| 20 | QLK | 1028 |
| 21 | All Nippon Airways | 1023 |
| 22 | VIV | 929 |
| 23 | Cathay Pacific | 900 |
| 24 | CXK | 892 |
| 25 | United Airlines | 889 |
| 26 | AEE | 882 |
| 27 | GLO | 882 |
| 28 | Air France | 871 |
| 29 | MXY | 864 |
| 30 | JetBlue | 850 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 145133 |
| 2 | 🇪🇸 ES | 10790 |
| 3 | 🇧🇷 BR | 9580 |
| 4 | 🇦🇺 AU | 9409 |
| 5 | 🇮🇳 IN | 9303 |
| 6 | 🇨🇦 CA | 9121 |
| 7 | 🇮🇹 IT | 8695 |
| 8 | 🇩🇪 DE | 8397 |
| 9 | 🇬🇧 GB | 7836 |
| 10 | 🇯🇵 JP | 6788 |
| 11 | 🇫🇷 FR | 6678 |
| 12 | 🇨🇴 CO | 6063 |
| 13 | 🇬🇷 GR | 4889 |
| 14 | 🇲🇽 MX | 4817 |
| 15 | 🇨🇭 CH | 4437 |
| 16 | 🇳🇴 NO | 4399 |
| 17 | 🇹🇷 TR | 4073 |
| 18 | 🇲🇾 MY | 3035 |
| 19 | 🇵🇱 PL | 2840 |
| 20 | 🇿🇦 ZA | 2737 |
| 21 | 🇳🇿 NZ | 2448 |
| 22 | 🇹🇭 TH | 2447 |
| 23 | 🇵🇭 PH | 2229 |
| 24 | 🇬🇹 GT | 2176 |
| 25 | 🇰🇷 KR | 2151 |
| 26 | 🇲🇦 MA | 1704 |
| 27 | 🇭🇷 HR | 1614 |
| 28 | 🇲🇪 ME | 1557 |
| 29 | 🇳🇱 NL | 1535 |
| 30 | 🇲🇴 MO | 1432 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3457 |
| 2 | Denver International Airport |  | US | 2799 |
| 3 | Tokyo International Airport |  | JP | 2132 |
| 4 | Guaymaral Airport |  | CO | 2094 |
| 5 | Indira Gandhi International Airport |  | IN | 2061 |
| 6 | Harry Reid International Airport |  | US | 2026 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1843 |
| 8 | Zurich Airport |  | CH | 1790 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1770 |
| 10 | La Aurora Airport |  | GT | 1681 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1554 |
| 12 | Chicago O'Hare International Airport |  | US | 1525 |
| 13 | El Dorado International Airport |  | CO | 1524 |
| 14 | Frankfurt am Main International Airport |  | DE | 1513 |
| 15 | Salt Lake City International Airport |  | US | 1506 |
| 16 | Macau International Airport |  | MO | 1432 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1394 |
| 18 | Congonhas Airport |  | BR | 1380 |
| 19 | Madrid Barajas International Airport |  | ES | 1326 |
| 20 | Capua Airport |  | IT | 1311 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1279 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1187 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1184 |
| 24 | Charlotte/Douglas International Airport |  | US | 1172 |
| 25 | Charles de Gaulle International Airport |  | FR | 1150 |
| 26 | Kuala Lumpur International Airport |  | MY | 1144 |
| 27 | Malpensa International Airport |  | IT | 1135 |
| 28 | Bengaluru International Airport |  | IN | 1103 |
| 29 | Ninoy Aquino International Airport |  | PH | 1048 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1039 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1035 |
| 32 | Barcelona International Airport |  | ES | 994 |
| 33 | Daniel K Inouye International Airport |  | US | 980 |
| 34 | Seattle-Tacoma International Airport |  | US | 978 |
| 35 | Viracopos International Airport |  | BR | 961 |
| 36 | Calgary International Airport |  | CA | 952 |
| 37 | Tenerife Norte Airport |  | ES | 939 |
| 38 | Reno/Tahoe International Airport |  | US | 936 |
| 39 | Oslo Gardermoen Airport |  | NO | 935 |
| 40 | Scottsdale Airport |  | US | 932 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 871 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 613 | 21m | 244 km | 2,581.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 402 | 24m | 225 km | 1,559.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 402 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 382 | 1h 9m | 770 km | 5,074.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 288 | 27m | 275 km | 1,364.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 246 | 19m | 165 km | 699.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 246 | 44m | 241 km | 1,021.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 231 | 1h 47m | 1,423 km | 5,669.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 219 | 26m | 215 km | 811.1 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 199 | 19m | 144 km | 495.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 197 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 196 | 31m | 369 km | 1,247.6 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 196 | 50m | 556 km | 1,878.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 189 | 1h 38m | 1,156 km | 3,770.5 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 185 | 24m | 218 km | 697.0 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPRRR | SPR | Szczecin-Goleniow Solidarność Airport (EPSC) | Poznań-Ławica Airport (EPPO) | 2026-08-03 10:14 UTC | 2026-08-03 10:40 UTC | 26m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-08-02 20:22 UTC | 2026-08-03 10:26 UTC | 14h 4m |
| DEDMI | DED | Stuttgart Airport (EDDS) | Mengen-Hohentengen Airport (EDTM) | 2026-08-03 09:20 UTC | 2026-08-03 10:23 UTC | 1h 3m |
| AWH45D | AWH | Hannover Airport (EDDV) | Oberrissdorf Airport (EDUO) | 2026-08-03 09:56 UTC | 2026-08-03 10:22 UTC | 26m |
| LOT2206 | LOT Polish Airlines | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Male Bielice Glider Airport (LZPT) | 2026-08-03 09:04 UTC | 2026-08-03 10:16 UTC | 1h 11m |
| LOT1KJ | LOT Polish Airlines | Malpensa International Airport (LIMC) | Zilina Airport (LZZI) | 2026-08-03 09:02 UTC | 2026-08-03 10:08 UTC | 1h 5m |
| MEA226 | Middle East Airlines | Copenhagen Kastrup Airport (EKCH) | EPCH (EPCH) | 2026-08-03 09:10 UTC | 2026-08-03 10:01 UTC | 51m |
| WIF1A | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-03 09:03 UTC | 2026-08-03 09:55 UTC | 52m |
| NAY55JR | NAY | Lanzarote Airport (GCRR) | Tenerife Norte Airport (GCXO) | 2026-08-03 09:25 UTC | 2026-08-03 09:54 UTC | 29m |
| RYR83RY | Ryanair | Paris Beauvais Tille Airport (LFOB) | Otocac Airport (LDRO) | 2026-08-03 08:31 UTC | 2026-08-03 09:53 UTC | 1h 22m |
| EZY59WD | easyJet | Amsterdam Airport Schiphol (EHAM) | London Gatwick Airport (EGKK) | 2026-08-03 08:03 UTC | 2026-08-03 09:53 UTC | 1h 49m |
| RYR4SP | Ryanair | London Stansted Airport (EGSS) | Malpensa International Airport (LIMC) | 2026-08-03 08:21 UTC | 2026-08-03 09:51 UTC | 1h 30m |
| EZY61HD | easyJet | Belfast International Airport (EGAA) | Coventry Airport (EGBE) | 2026-08-03 08:58 UTC | 2026-08-03 09:50 UTC | 52m |
| IGO254J | IndiGo | Indira Gandhi International Airport (VIDP) | Meghauli Airport (VNMG) | 2026-08-03 08:55 UTC | 2026-08-03 09:48 UTC | 52m |
| HBXPD | HBX | Samedan Airport (LSZS) | Ambri Airport (LSPM) | 2026-08-03 09:25 UTC | 2026-08-03 09:46 UTC | 21m |
| VLG9FT | Vueling | Palma De Mallorca Airport (LEPA) | Federico Garcia Lorca Airport (LEGR) | 2026-08-03 08:51 UTC | 2026-08-03 09:46 UTC | 55m |
| AXM464 | AXM | Kuala Lumpur International Airport (WMKK) | Bentayan Airport (WIPY) | 2026-08-03 08:53 UTC | 2026-08-03 09:43 UTC | 50m |
| AEE590 | AEE | Thessaloniki Macedonia International Airport (LGTS) | Santorini Airport (LGSR) | 2026-08-03 08:34 UTC | 2026-08-03 09:43 UTC | 1h 9m |
| IGO502F | IndiGo | Indira Gandhi International Airport (VIDP) | Chandigarh Airport (VICG) | 2026-08-03 09:14 UTC | 2026-08-03 09:42 UTC | 27m |
| VJH724 | VJH | Zurich Airport (LSZH) | Ostrava Leos Janacek Airport (LKMT) | 2026-08-03 08:37 UTC | 2026-08-03 09:41 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
