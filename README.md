# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_18:10:31_UTC-green)

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

**Latest saved flight:** 2026-07-09 18:10:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-09 18:10:31 UTC

- **134,422** saved flights
- **45,483** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **134,422** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,617,399.1 tonnes** estimated CO2 emissions
- **93,762,265 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5461 |
| 2 | SkyWest Airlines | 4950 |
| 3 | EJA | 2628 |
| 4 | IndiGo | 2498 |
| 5 | American Airlines | 2098 |
| 6 | Southwest Airlines | 2019 |
| 7 | ENY | 1685 |
| 8 | Delta Air Lines | 1603 |
| 9 | Lufthansa | 1388 |
| 10 | LATAM Airlines | 1233 |
| 11 | Vueling | 1177 |
| 12 | WIF | 1171 |
| 13 | AZU | 1144 |
| 14 | LXJ | 1032 |
| 15 | AXM | 1021 |
| 16 | Swiss International | 956 |
| 17 | All Nippon Airways | 878 |
| 18 | easyJet | 871 |
| 19 | Alaska Airlines | 852 |
| 20 | QLK | 841 |
| 21 | EJU | 828 |
| 22 | VIV | 740 |
| 23 | AEE | 732 |
| 24 | CXK | 723 |
| 25 | Air France | 722 |
| 26 | Cathay Pacific | 720 |
| 27 | United Airlines | 710 |
| 28 | JetBlue | 708 |
| 29 | MXY | 695 |
| 30 | GLO | 684 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 115214 |
| 2 | 🇪🇸 ES | 8919 |
| 3 | 🇮🇳 IN | 7835 |
| 4 | 🇦🇺 AU | 7766 |
| 5 | 🇧🇷 BR | 7566 |
| 6 | 🇨🇦 CA | 7087 |
| 7 | 🇩🇪 DE | 7020 |
| 8 | 🇮🇹 IT | 6988 |
| 9 | 🇬🇧 GB | 6058 |
| 10 | 🇯🇵 JP | 5755 |
| 11 | 🇫🇷 FR | 5343 |
| 12 | 🇨🇴 CO | 4211 |
| 13 | 🇲🇽 MX | 3903 |
| 14 | 🇬🇷 GR | 3845 |
| 15 | 🇳🇴 NO | 3650 |
| 16 | 🇨🇭 CH | 3483 |
| 17 | 🇹🇷 TR | 3059 |
| 18 | 🇲🇾 MY | 2651 |
| 19 | 🇵🇱 PL | 2226 |
| 20 | 🇿🇦 ZA | 2217 |
| 21 | 🇳🇿 NZ | 2103 |
| 22 | 🇹🇭 TH | 2062 |
| 23 | 🇰🇷 KR | 1984 |
| 24 | 🇵🇭 PH | 1850 |
| 25 | 🇬🇹 GT | 1819 |
| 26 | 🇲🇦 MA | 1425 |
| 27 | 🇲🇪 ME | 1341 |
| 28 | 🇳🇱 NL | 1259 |
| 29 | 🇭🇷 HR | 1198 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2796 |
| 2 | Denver International Airport |  | US | 2266 |
| 3 | Tokyo International Airport |  | JP | 1878 |
| 4 | Indira Gandhi International Airport |  | IN | 1733 |
| 5 | Harry Reid International Airport |  | US | 1670 |
| 6 | Guaymaral Airport |  | CO | 1644 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1578 |
| 8 | Zurich Airport |  | CH | 1496 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1423 |
| 10 | La Aurora Airport |  | GT | 1405 |
| 11 | Frankfurt am Main International Airport |  | DE | 1343 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1294 |
| 13 | Chicago O'Hare International Airport |  | US | 1280 |
| 14 | Salt Lake City International Airport |  | US | 1194 |
| 15 | El Dorado International Airport |  | CO | 1191 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1161 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1099 |
| 19 | Madrid Barajas International Airport |  | ES | 1099 |
| 20 | Capua Airport |  | IT | 1099 |
| 21 | Congonhas Airport |  | BR | 1071 |
| 22 | Kuala Lumpur International Airport |  | MY | 1030 |
| 23 | Charlotte/Douglas International Airport |  | US | 990 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 975 |
| 25 | Charles de Gaulle International Airport |  | FR | 962 |
| 26 | Bengaluru International Airport |  | IN | 943 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 923 |
| 28 | Malpensa International Airport |  | IT | 887 |
| 29 | Ninoy Aquino International Airport |  | PH | 861 |
| 30 | Daniel K Inouye International Airport |  | US | 836 |
| 31 | Barcelona International Airport |  | ES | 827 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 818 |
| 33 | Tenerife Norte Airport |  | ES | 806 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 788 |
| 35 | Calgary International Airport |  | CA | 778 |
| 36 | Seattle-Tacoma International Airport |  | US | 768 |
| 37 | Scottsdale Airport |  | US | 768 |
| 38 | Viracopos International Airport |  | BR | 766 |
| 39 | Vitoria/Foronda Airport |  | ES | 761 |
| 40 | Amsterdam Airport Schiphol |  | NL | 756 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 692 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 487 | 21m | 244 km | 2,050.6 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 336 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 324 | 1h 10m | 770 km | 4,304.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 288 | 14m | 114 km | 564.9 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 244 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 196 | 22m | 55 km | 186.3 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 187 | 26m | 215 km | 692.6 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 182 | 1h 46m | 1,423 km | 4,466.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 163 | 20m | 250 km | 704.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 160 | 44m | 452 km | 1,247.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 156 | 1h 16m | 961 km | 2,585.8 t |
| 27 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 154 | 1h 38m | 1,156 km | 3,072.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N73345 |  | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-07-09 17:52 UTC | 2026-07-09 18:10 UTC | 17m |
| BB033 |  | Skypark Estates Owners Assoc Airport (18FD) | South Alabama Regional At Bill Benton Field (K79J) | 2026-07-09 17:43 UTC | 2026-07-09 18:10 UTC | 26m |
| N4776E |  | Clearwater Executive Airport (KCLW) | Clearwater Executive Airport (KCLW) | 2026-07-09 17:12 UTC | 2026-07-09 18:04 UTC | 51m |
|  |  | Conroe/North Houston Regional Airport (KCXO) | Livingston Municipal Airport (K00R) | 2026-07-09 17:51 UTC | 2026-07-09 18:02 UTC | 10m |
| PREY21 | PRE | Victoria Regional Airport (KVCT) | Kenedy Regional Airport (K2R9) | 2026-07-09 17:32 UTC | 2026-07-09 18:01 UTC | 29m |
| N2454E |  | Grand Prairie Municipal Airport (KGPM) | 20TE (20TE) | 2026-07-09 17:30 UTC | 2026-07-09 18:01 UTC | 31m |
| N445BG |  | Wood County Airport (K1G0) | Bluffton Airport (K5G7) | 2026-07-09 17:23 UTC | 2026-07-09 18:01 UTC | 38m |
| SWOOP41 | SWO | 2TX3 (2TX3) | Benson Airstrip (2XS8) | 2026-07-09 17:40 UTC | 2026-07-09 17:59 UTC | 18m |
| COBRA11 | COB | Jones Farm Field (OK12) | Ramsak Airport (OK67) | 2026-07-09 17:34 UTC | 2026-07-09 17:57 UTC | 22m |
| KNM08 | KNM | Chichester/Goodwood Airport (EGHR) | Wolverhampton Halfpenny Green Airport (EGBO) | 2026-07-09 17:07 UTC | 2026-07-09 17:57 UTC | 50m |
| AAL1451 | American Airlines | Los Angeles International Airport (KLAX) | Philadelphia International Airport (KPHL) | 2026-07-09 13:25 UTC | 2026-07-09 17:57 UTC | 4h 31m |
| N537AR |  | Baker & Hall Airport (77CL) | Table Mountain Field (5CL9) | 2026-07-09 16:11 UTC | 2026-07-09 17:56 UTC | 1h 45m |
| N5421K |  | Denton Enterprise Airport (KDTO) | Gainesville Municipal Airport (KGLE) | 2026-07-09 17:29 UTC | 2026-07-09 17:55 UTC | 26m |
| N236FY |  | Merritt Island Airport (KCOI) | Merritt Island Airport (KCOI) | 2026-07-09 16:22 UTC | 2026-07-09 17:55 UTC | 1h 33m |
| BOE364 | BOE | Boeing Field/King County International Airport (KBFI) | Warden Airport (K2S4) | 2026-07-09 16:33 UTC | 2026-07-09 17:54 UTC | 1h 21m |
| N472D |  | Auburn University Regional Airport (KAUO) | Thomas C Russell Field (KALX) | 2026-07-09 17:18 UTC | 2026-07-09 17:54 UTC | 36m |
| QTR54M | Qatar Airways | Antalya International Airport (LTAI) | Zirku Airport (OMAZ) | 2026-07-09 10:24 UTC | 2026-07-09 17:53 UTC | 7h 29m |
| ERU48 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | Prescott Regional/Ernest A Love Field (KPRC) | 2026-07-09 17:38 UTC | 2026-07-09 17:51 UTC | 12m |
| N781JH |  | Waterloo Regional Airport (KALO) | Angen Field (MN44) | 2026-07-09 17:14 UTC | 2026-07-09 17:50 UTC | 36m |
| N2368P |  | Daytona Beach International Airport (KDAB) | Ormond Beach Municipal Airport (KOMN) | 2026-07-09 17:32 UTC | 2026-07-09 17:49 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
