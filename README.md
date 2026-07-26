# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_11:38:54_UTC-green)

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

**Latest saved flight:** 2026-07-26 11:38:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-26 11:38:54 UTC

- **151,888** saved flights
- **50,411** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **151,888** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,818,248.5 tonnes** estimated CO2 emissions
- **105,405,709 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6127 |
| 2 | SkyWest Airlines | 5554 |
| 3 | EJA | 3000 |
| 4 | IndiGo | 2715 |
| 5 | American Airlines | 2410 |
| 6 | Southwest Airlines | 2310 |
| 7 | ENY | 1895 |
| 8 | Delta Air Lines | 1781 |
| 9 | Lufthansa | 1483 |
| 10 | LATAM Airlines | 1404 |
| 11 | AZU | 1317 |
| 12 | WIF | 1278 |
| 13 | Vueling | 1272 |
| 14 | LXJ | 1168 |
| 15 | AXM | 1088 |
| 16 | Swiss International | 1067 |
| 17 | easyJet | 991 |
| 18 | All Nippon Airways | 960 |
| 19 | Alaska Airlines | 949 |
| 20 | QLK | 941 |
| 21 | EJU | 932 |
| 22 | VIV | 835 |
| 23 | CXK | 811 |
| 24 | AEE | 798 |
| 25 | MXY | 795 |
| 26 | Air France | 792 |
| 27 | JetBlue | 790 |
| 28 | GLO | 788 |
| 29 | Cathay Pacific | 784 |
| 30 | United Airlines | 784 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 130883 |
| 2 | 🇪🇸 ES | 9820 |
| 3 | 🇧🇷 BR | 8597 |
| 4 | 🇦🇺 AU | 8593 |
| 5 | 🇮🇳 IN | 8540 |
| 6 | 🇨🇦 CA | 8095 |
| 7 | 🇮🇹 IT | 7865 |
| 8 | 🇩🇪 DE | 7777 |
| 9 | 🇬🇧 GB | 6968 |
| 10 | 🇯🇵 JP | 6312 |
| 11 | 🇫🇷 FR | 6021 |
| 12 | 🇨🇴 CO | 5172 |
| 13 | 🇲🇽 MX | 4373 |
| 14 | 🇬🇷 GR | 4319 |
| 15 | 🇳🇴 NO | 4010 |
| 16 | 🇨🇭 CH | 3996 |
| 17 | 🇹🇷 TR | 3613 |
| 18 | 🇲🇾 MY | 2836 |
| 19 | 🇵🇱 PL | 2594 |
| 20 | 🇿🇦 ZA | 2472 |
| 21 | 🇳🇿 NZ | 2289 |
| 22 | 🇹🇭 TH | 2209 |
| 23 | 🇰🇷 KR | 2077 |
| 24 | 🇵🇭 PH | 2021 |
| 25 | 🇬🇹 GT | 1976 |
| 26 | 🇲🇦 MA | 1546 |
| 27 | 🇲🇪 ME | 1486 |
| 28 | 🇳🇱 NL | 1397 |
| 29 | 🇭🇷 HR | 1395 |
| 30 | 🇲🇴 MO | 1253 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3128 |
| 2 | Denver International Airport |  | US | 2547 |
| 3 | Tokyo International Airport |  | JP | 2005 |
| 4 | Guaymaral Airport |  | CO | 1906 |
| 5 | Indira Gandhi International Airport |  | IN | 1896 |
| 6 | Harry Reid International Airport |  | US | 1873 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1701 |
| 8 | Zurich Airport |  | CH | 1656 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1587 |
| 10 | La Aurora Airport |  | GT | 1531 |
| 11 | Frankfurt am Main International Airport |  | DE | 1431 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1420 |
| 13 | Chicago O'Hare International Airport |  | US | 1398 |
| 14 | El Dorado International Airport |  | CO | 1368 |
| 15 | Salt Lake City International Airport |  | US | 1365 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1295 |
| 17 | Macau International Airport |  | MO | 1253 |
| 18 | Congonhas Airport |  | BR | 1229 |
| 19 | Madrid Barajas International Airport |  | ES | 1213 |
| 20 | Capua Airport |  | IT | 1207 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1174 |
| 22 | Kuala Lumpur International Airport |  | MY | 1090 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1087 |
| 24 | Charlotte/Douglas International Airport |  | US | 1079 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1069 |
| 26 | Charles de Gaulle International Airport |  | FR | 1043 |
| 27 | Bengaluru International Airport |  | IN | 1021 |
| 28 | Malpensa International Airport |  | IT | 996 |
| 29 | Ninoy Aquino International Airport |  | PH | 946 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 917 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 909 |
| 32 | Barcelona International Airport |  | ES | 907 |
| 33 | Daniel K Inouye International Airport |  | US | 906 |
| 34 | Tenerife Norte Airport |  | ES | 876 |
| 35 | Seattle-Tacoma International Airport |  | US | 875 |
| 36 | Calgary International Airport |  | CA | 862 |
| 37 | Viracopos International Airport |  | BR | 857 |
| 38 | Scottsdale Airport |  | US | 855 |
| 39 | Amsterdam Airport Schiphol |  | NL | 840 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 832 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 804 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 550 | 21m | 244 km | 2,315.9 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 369 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 368 | 24m | 225 km | 1,427.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 355 | 1h 9m | 770 km | 4,715.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 278 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 273 | 27m | 275 km | 1,293.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 205 | 1h 47m | 1,423 km | 5,031.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 199 | 26m | 215 km | 737.0 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 198 | 20m | 99 km | 339.2 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 184 | 30m | 49 km | 155.5 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 184 | 27m | 152 km | 480.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 180 | 1h 15m | 961 km | 2,983.6 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 178 | 31m | 369 km | 1,133.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 178 | 18m | 144 km | 442.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 178 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 171 | 1h 39m | 1,156 km | 3,411.4 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 168 | 51m | 556 km | 1,610.4 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DESFM | DES | Mengen-Hohentengen Airport (EDTM) | Mengen-Hohentengen Airport (EDTM) | 2026-07-26 11:18 UTC | 2026-07-26 11:38 UTC | 20m |
| N21754 |  | Orlando Apopka Airport (KX04) | Leesburg International Airport (KLEE) | 2026-07-26 11:20 UTC | 2026-07-26 11:31 UTC | 10m |
| PTN21V | PTN | Faro Airport (LPFR) | Nice-Cote d'Azur Airport (LFMN) | 2026-07-26 09:01 UTC | 2026-07-26 11:24 UTC | 2h 23m |
| HK4384 |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-07-26 11:02 UTC | 2026-07-26 11:12 UTC | 10m |
| PJV650 | PJV | Nice-Cote d'Azur Airport (LFMN) | Napoli / Capodichino International Airport (LIRN) | 2026-07-26 10:19 UTC | 2026-07-26 11:11 UTC | 51m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-26 10:41 UTC | 2026-07-26 11:10 UTC | 28m |
| SHA828 | SHA | Langtang Airport (VNLT) | Langtang Airport (VNLT) | 2026-07-26 11:01 UTC | 2026-07-26 11:02 UTC | 0m |
| AWH32B | AWH | Hannover Airport (EDDV) | Brussels Airport (EBBR) | 2026-07-26 10:05 UTC | 2026-07-26 10:54 UTC | 48m |
| PSPEL | PSP | Aeroporto Elias Breder Airport (SNJM) | Eurico de Aguiar Salles Airport (SBVT) | 2026-07-26 10:26 UTC | 2026-07-26 10:53 UTC | 27m |
| NWS322 | NWS | Spichenkovo Airport (UNWW) | Kasimovo Airfield (XLLN) | 2026-07-26 06:22 UTC | 2026-07-26 10:48 UTC | 4h 25m |
| AWG729 | AWG | Istanbul Airport (LTFM) | Cluj-Napoca International Airport (LRCL) | 2026-07-26 09:43 UTC | 2026-07-26 10:47 UTC | 1h 4m |
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-07-26 09:13 UTC | 2026-07-26 10:46 UTC | 1h 33m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-07-26 10:30 UTC | 2026-07-26 10:46 UTC | 16m |
| SPHOR | SPH | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-07-26 10:40 UTC | 2026-07-26 10:46 UTC | 5m |
| EXS32VA | EXS | Manchester Airport (EGCC) | Dubrovnik Airport (LDDU) | 2026-07-26 08:15 UTC | 2026-07-26 10:42 UTC | 2h 26m |
| ESEN01 | ESE | Ataturk International Airport (LTBA) | Suleyman Demirel International Airport (LTFC) | 2026-07-26 10:03 UTC | 2026-07-26 10:37 UTC | 34m |
| N142NE |  | General Edward Lawrence Logan International Airport (KBOS) | Lawrence Municipal Airport (KLWM) | 2026-07-26 10:21 UTC | 2026-07-26 10:35 UTC | 13m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-07-26 09:59 UTC | 2026-07-26 10:34 UTC | 34m |
| THY1SG | Turkish Airlines | Istanbul Airport (LTFM) | Kutahya Airport (LTBN) | 2026-07-26 10:08 UTC | 2026-07-26 10:32 UTC | 24m |
| MNE311 | MNE | Zurich Airport (LSZH) | Tivat Airport (LYTV) | 2026-07-26 09:16 UTC | 2026-07-26 10:32 UTC | 1h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
