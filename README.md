# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_16:59:52_UTC-green)

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

**Latest saved flight:** 2026-07-05 16:59:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-05 16:59:52 UTC

- **129,996** saved flights
- **44,204** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **129,996** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,568,873.5 tonnes** estimated CO2 emissions
- **90,949,188 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5292 |
| 2 | SkyWest Airlines | 4808 |
| 3 | EJA | 2545 |
| 4 | IndiGo | 2441 |
| 5 | American Airlines | 2003 |
| 6 | Southwest Airlines | 1954 |
| 7 | ENY | 1632 |
| 8 | Delta Air Lines | 1561 |
| 9 | Lufthansa | 1366 |
| 10 | LATAM Airlines | 1185 |
| 11 | Vueling | 1154 |
| 12 | WIF | 1138 |
| 13 | AZU | 1106 |
| 14 | AXM | 1009 |
| 15 | LXJ | 1001 |
| 16 | Swiss International | 910 |
| 17 | All Nippon Airways | 860 |
| 18 | Alaska Airlines | 836 |
| 19 | easyJet | 831 |
| 20 | QLK | 816 |
| 21 | EJU | 804 |
| 22 | VIV | 721 |
| 23 | Cathay Pacific | 713 |
| 24 | AEE | 708 |
| 25 | Air France | 707 |
| 26 | CXK | 697 |
| 27 | United Airlines | 692 |
| 28 | JetBlue | 680 |
| 29 | MXY | 679 |
| 30 | GLO | 664 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 111202 |
| 2 | 🇪🇸 ES | 8680 |
| 3 | 🇮🇳 IN | 7650 |
| 4 | 🇦🇺 AU | 7519 |
| 5 | 🇧🇷 BR | 7309 |
| 6 | 🇨🇦 CA | 6850 |
| 7 | 🇩🇪 DE | 6831 |
| 8 | 🇮🇹 IT | 6799 |
| 9 | 🇬🇧 GB | 5780 |
| 10 | 🇯🇵 JP | 5624 |
| 11 | 🇫🇷 FR | 5178 |
| 12 | 🇨🇴 CO | 4098 |
| 13 | 🇲🇽 MX | 3799 |
| 14 | 🇬🇷 GR | 3711 |
| 15 | 🇳🇴 NO | 3535 |
| 16 | 🇨🇭 CH | 3348 |
| 17 | 🇹🇷 TR | 2853 |
| 18 | 🇲🇾 MY | 2616 |
| 19 | 🇿🇦 ZA | 2157 |
| 20 | 🇵🇱 PL | 2137 |
| 21 | 🇳🇿 NZ | 2080 |
| 22 | 🇹🇭 TH | 2014 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1813 |
| 25 | 🇬🇹 GT | 1773 |
| 26 | 🇲🇦 MA | 1389 |
| 27 | 🇲🇪 ME | 1290 |
| 28 | 🇳🇱 NL | 1221 |
| 29 | 🇲🇴 MO | 1185 |
| 30 | 🇭🇷 HR | 1138 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2709 |
| 2 | Denver International Airport |  | US | 2205 |
| 3 | Tokyo International Airport |  | JP | 1851 |
| 4 | Indira Gandhi International Airport |  | IN | 1688 |
| 5 | Harry Reid International Airport |  | US | 1614 |
| 6 | Guaymaral Airport |  | CO | 1583 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1539 |
| 8 | Zurich Airport |  | CH | 1436 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1384 |
| 10 | La Aurora Airport |  | GT | 1372 |
| 11 | Frankfurt am Main International Airport |  | DE | 1322 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1260 |
| 13 | Chicago O'Hare International Airport |  | US | 1247 |
| 14 | Macau International Airport |  | MO | 1185 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1155 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1100 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1070 |
| 19 | Madrid Barajas International Airport |  | ES | 1068 |
| 20 | Capua Airport |  | IT | 1067 |
| 21 | Congonhas Airport |  | BR | 1033 |
| 22 | Kuala Lumpur International Airport |  | MY | 1015 |
| 23 | Charlotte/Douglas International Airport |  | US | 970 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 950 |
| 25 | Charles de Gaulle International Airport |  | FR | 943 |
| 26 | Bengaluru International Airport |  | IN | 926 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 879 |
| 28 | Malpensa International Airport |  | IT | 878 |
| 29 | Ninoy Aquino International Airport |  | PH | 841 |
| 30 | Daniel K Inouye International Airport |  | US | 817 |
| 31 | Barcelona International Airport |  | ES | 807 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 794 |
| 33 | Tenerife Norte Airport |  | ES | 787 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 760 |
| 35 | Calgary International Airport |  | CA | 755 |
| 36 | Vitoria/Foronda Airport |  | ES | 750 |
| 37 | Seattle-Tacoma International Airport |  | US | 748 |
| 38 | Viracopos International Airport |  | BR | 745 |
| 39 | Scottsdale Airport |  | US | 745 |
| 40 | Amsterdam Airport Schiphol |  | NL | 738 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 664 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 470 | 21m | 244 km | 1,979.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 327 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 315 | 1h 10m | 770 km | 4,184.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 240 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 183 | 44m | 241 km | 760.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 174 | 27m | 152 km | 454.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 168 | 1h 45m | 1,423 km | 4,123.0 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 160 | 18m | 144 km | 398.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 159 | 20m | 250 km | 686.8 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 26 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 152 | 1h 16m | 961 km | 2,519.5 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 150 | 54m | 136 km | 351.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 148 | 1h 38m | 1,156 km | 2,952.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 145 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N2733G |  | Addington Field (KEKX) | Addington Field (KEKX) | 2026-07-05 16:39 UTC | 2026-07-05 16:59 UTC | 20m |
| CAP609 | CAP | Groton-New London Airport (KGON) | Westmoreland Airport (49NY) | 2026-07-05 14:30 UTC | 2026-07-05 16:58 UTC | 2h 27m |
| FDB1626 | flydubai | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-07-05 16:44 UTC | 2026-07-05 16:56 UTC | 12m |
| ICG35 | ICG | Kaldarmelar Airport (BIKA) | Reykjavik Airport (BIRK) | 2026-07-05 16:37 UTC | 2026-07-05 16:52 UTC | 15m |
| N1910R |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-07-05 16:26 UTC | 2026-07-05 16:52 UTC | 25m |
| N501HV |  | Cedar Creek Airport (2OH4) | Cedar Creek Airport (2OH4) | 2026-07-05 16:14 UTC | 2026-07-05 16:52 UTC | 37m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-07-05 16:12 UTC | 2026-07-05 16:49 UTC | 36m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-05 16:00 UTC | 2026-07-05 16:47 UTC | 46m |
| N6512K |  | Fairfield County Airport (KLHQ) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-05 15:16 UTC | 2026-07-05 16:42 UTC | 1h 25m |
| N7308G |  | Blairstown Airport (K1N7) | Blairstown Airport (K1N7) | 2026-07-05 16:21 UTC | 2026-07-05 16:40 UTC | 19m |
| N642SP |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-07-05 16:37 UTC | 2026-07-05 16:40 UTC | 2m |
| N682AC |  | Garrett Ranch Airport (77XS) | Bb Airpark (TE88) | 2026-07-05 16:26 UTC | 2026-07-05 16:37 UTC | 10m |
| HK5220 |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-05 16:03 UTC | 2026-07-05 16:34 UTC | 30m |
| UAL394 | United Airlines | Denver International Airport (KDEN) | Fairview Airport (CEB5) | 2026-07-05 13:57 UTC | 2026-07-05 16:34 UTC | 2h 37m |
| N95RJ |  | Brockville - Thousand Islands Regional Tackaberry Airport (CNL3) | Heritage Field (KPTW) | 2026-07-05 15:37 UTC | 2026-07-05 16:32 UTC | 54m |
| TRF688 | TRF | Addison Airport (KADS) | Mesquite Metro Airport (KHQZ) | 2026-07-05 16:14 UTC | 2026-07-05 16:26 UTC | 11m |
| SCU8 | SCU | 84OL (84OL) | William R Pogue Municipal Airport (KOWP) | 2026-07-05 16:04 UTC | 2026-07-05 16:26 UTC | 21m |
| CXK215 | CXK | Mckinney Ntl Airport (KTKI) | 31TS (31TS) | 2026-07-05 16:12 UTC | 2026-07-05 16:24 UTC | 12m |
| N267JL |  | Richland Municipal Airport (KMO1) | Troy Municipal At N Kenneth Campbell Field (KTOI) | 2026-07-05 15:08 UTC | 2026-07-05 16:22 UTC | 1h 13m |
| AXB36N | AXB | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-07-05 14:59 UTC | 2026-07-05 16:21 UTC | 1h 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
