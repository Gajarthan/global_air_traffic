# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_14:25:43_UTC-green)

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

**Latest saved flight:** 2026-08-04 14:25:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-04 14:25:43 UTC

- **170,395** saved flights
- **55,508** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **170,395** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,054,369.0 tonnes** estimated CO2 emissions
- **119,093,855 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6785 |
| 2 | SkyWest Airlines | 6223 |
| 3 | EJA | 3380 |
| 4 | IndiGo | 2999 |
| 5 | American Airlines | 2681 |
| 6 | Southwest Airlines | 2681 |
| 7 | ENY | 2124 |
| 8 | Delta Air Lines | 2027 |
| 9 | LATAM Airlines | 1579 |
| 10 | Lufthansa | 1563 |
| 11 | AZU | 1501 |
| 12 | WIF | 1425 |
| 13 | Vueling | 1405 |
| 14 | LXJ | 1335 |
| 15 | AXM | 1176 |
| 16 | Swiss International | 1162 |
| 17 | easyJet | 1146 |
| 18 | EJU | 1044 |
| 19 | Alaska Airlines | 1041 |
| 20 | QLK | 1041 |
| 21 | All Nippon Airways | 1036 |
| 22 | VIV | 941 |
| 23 | Cathay Pacific | 913 |
| 24 | CXK | 905 |
| 25 | United Airlines | 896 |
| 26 | AEE | 892 |
| 27 | GLO | 890 |
| 28 | Air France | 875 |
| 29 | MXY | 869 |
| 30 | JetBlue | 855 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 146742 |
| 2 | 🇪🇸 ES | 10926 |
| 3 | 🇧🇷 BR | 9683 |
| 4 | 🇦🇺 AU | 9521 |
| 5 | 🇮🇳 IN | 9397 |
| 6 | 🇨🇦 CA | 9247 |
| 7 | 🇮🇹 IT | 8815 |
| 8 | 🇩🇪 DE | 8491 |
| 9 | 🇬🇧 GB | 7911 |
| 10 | 🇯🇵 JP | 6871 |
| 11 | 🇫🇷 FR | 6764 |
| 12 | 🇨🇴 CO | 6186 |
| 13 | 🇬🇷 GR | 4963 |
| 14 | 🇲🇽 MX | 4871 |
| 15 | 🇨🇭 CH | 4488 |
| 16 | 🇳🇴 NO | 4448 |
| 17 | 🇹🇷 TR | 4161 |
| 18 | 🇲🇾 MY | 3057 |
| 19 | 🇵🇱 PL | 2869 |
| 20 | 🇿🇦 ZA | 2761 |
| 21 | 🇹🇭 TH | 2486 |
| 22 | 🇳🇿 NZ | 2471 |
| 23 | 🇵🇭 PH | 2253 |
| 24 | 🇬🇹 GT | 2192 |
| 25 | 🇰🇷 KR | 2161 |
| 26 | 🇲🇦 MA | 1718 |
| 27 | 🇭🇷 HR | 1641 |
| 28 | 🇲🇪 ME | 1572 |
| 29 | 🇳🇱 NL | 1548 |
| 30 | 🇲🇴 MO | 1456 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3505 |
| 2 | Denver International Airport |  | US | 2820 |
| 3 | Tokyo International Airport |  | JP | 2156 |
| 4 | Guaymaral Airport |  | CO | 2107 |
| 5 | Indira Gandhi International Airport |  | IN | 2082 |
| 6 | Harry Reid International Airport |  | US | 2048 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1864 |
| 8 | Zurich Airport |  | CH | 1804 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1791 |
| 10 | La Aurora Airport |  | GT | 1691 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1570 |
| 12 | El Dorado International Airport |  | CO | 1547 |
| 13 | Chicago O'Hare International Airport |  | US | 1545 |
| 14 | Salt Lake City International Airport |  | US | 1528 |
| 15 | Frankfurt am Main International Airport |  | DE | 1525 |
| 16 | Macau International Airport |  | MO | 1456 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1401 |
| 18 | Congonhas Airport |  | BR | 1392 |
| 19 | Madrid Barajas International Airport |  | ES | 1335 |
| 20 | Capua Airport |  | IT | 1329 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1289 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1202 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1193 |
| 24 | Charlotte/Douglas International Airport |  | US | 1183 |
| 25 | Charles de Gaulle International Airport |  | FR | 1155 |
| 26 | Kuala Lumpur International Airport |  | MY | 1151 |
| 27 | Malpensa International Airport |  | IT | 1147 |
| 28 | Bengaluru International Airport |  | IN | 1119 |
| 29 | Ninoy Aquino International Airport |  | PH | 1060 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1057 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1051 |
| 32 | Barcelona International Airport |  | ES | 1009 |
| 33 | Daniel K Inouye International Airport |  | US | 988 |
| 34 | Seattle-Tacoma International Airport |  | US | 984 |
| 35 | Viracopos International Airport |  | BR | 970 |
| 36 | Calgary International Airport |  | CA | 964 |
| 37 | Reno/Tahoe International Airport |  | US | 953 |
| 38 | Oslo Gardermoen Airport |  | NO | 948 |
| 39 | Tenerife Norte Airport |  | ES | 948 |
| 40 | Scottsdale Airport |  | US | 936 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 875 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 621 | 21m | 244 km | 2,614.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 405 | 24m | 225 km | 1,571.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 403 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 387 | 1h 8m | 770 km | 5,141.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 290 | 27m | 275 km | 1,374.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 255 | 22m | 55 km | 242.4 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 253 | 44m | 241 km | 1,050.9 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 234 | 1h 47m | 1,423 km | 5,742.7 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 220 | 26m | 215 km | 814.8 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 215 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 201 | 1h 15m | 961 km | 3,331.7 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 201 | 50m | 556 km | 1,926.8 t |
| 24 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 199 | 12m | - | - |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 192 | 1h 38m | 1,156 km | 3,830.3 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 187 | 24m | 218 km | 704.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 186 | 1h 1m | 695 km | 2,229.6 t |
| 30 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 185 | 8m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LFA546 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-08-04 13:36 UTC | 2026-08-04 14:25 UTC | 49m |
| N5518W |  | Cherokee Ranch Airport (OK25) | Gregg Airport (7OK1) | 2026-08-04 14:11 UTC | 2026-08-04 14:24 UTC | 12m |
| N844MK |  | Trenton Mercer Airport (KTTN) | Newark Liberty International Airport (KEWR) | 2026-08-04 13:59 UTC | 2026-08-04 14:20 UTC | 21m |
| N56BH |  | Sky Harbor Residential Airpark (1MN8) | Airlake Airport (KLVN) | 2026-08-04 13:22 UTC | 2026-08-04 14:20 UTC | 57m |
| CXK496 | CXK | Denton Enterprise Airport (KDTO) | Addington Field (4TX8) | 2026-08-04 13:58 UTC | 2026-08-04 14:15 UTC | 17m |
| N105RF |  | Tannehill Airfield (MI60) | 1MI8 (1MI8) | 2026-08-04 13:06 UTC | 2026-08-04 14:15 UTC | 1h 8m |
| HBSHA | HBS | St Gallen Altenrhein Airport (LSZR) | Friedrichshafen Airport (EDNY) | 2026-08-04 13:14 UTC | 2026-08-04 14:13 UTC | 59m |
| CXK582 | CXK | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-04 13:55 UTC | 2026-08-04 14:11 UTC | 16m |
| N262WJ |  | South Haven Area Regional Airport (KLWA) | South Haven Area Regional Airport (KLWA) | 2026-08-04 14:04 UTC | 2026-08-04 14:11 UTC | 6m |
| N333CT |  | St George Regional Airport (KSGU) | St George Regional Airport (KSGU) | 2026-08-04 13:37 UTC | 2026-08-04 14:09 UTC | 31m |
| N266AG |  | Morrisonville International Airport (WN85) | Eberle Ranch Airport (5WN2) | 2026-08-04 12:10 UTC | 2026-08-04 14:07 UTC | 1h 57m |
| N9161T |  | North Texas Regional/Perrin Field (KGYI) | Jones Field (KF00) | 2026-08-04 12:45 UTC | 2026-08-04 14:05 UTC | 1h 20m |
| 494LG |  | Simonson Field (80CO) | Silver West Airport (KC08) | 2026-08-04 13:48 UTC | 2026-08-04 14:05 UTC | 16m |
| N895SF |  | Skydive New England Airport (ME64) | Skydive New England Airport (ME64) | 2026-08-04 13:48 UTC | 2026-08-04 14:03 UTC | 15m |
| RJA521 | Royal Jordanian | Queen Alia International Airport (OJAI) | Mitiga Airport (HLLM) | 2026-08-04 11:18 UTC | 2026-08-04 14:03 UTC | 2h 44m |
| N884HB |  | St George Regional Airport (KSGU) | Blanding Municipal Airport (KBDG) | 2026-08-04 13:10 UTC | 2026-08-04 14:01 UTC | 51m |
| N366VR |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-08-04 13:31 UTC | 2026-08-04 13:59 UTC | 27m |
| ITIKE | ITI | Ghedi Airport (LIPL) | Milano / Bresso Airport (LIMB) | 2026-08-04 13:32 UTC | 2026-08-04 13:52 UTC | 20m |
| QTR8440 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-08-04 06:18 UTC | 2026-08-04 13:50 UTC | 7h 32m |
| N562X |  | Spiering Airport (8MD4) | Belfair Airport (DE32) | 2026-08-04 13:14 UTC | 2026-08-04 13:49 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
