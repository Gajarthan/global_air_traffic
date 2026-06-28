# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_18:29:44_UTC-green)

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

**Latest saved flight:** 2026-06-28 18:29:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-28 18:29:44 UTC

- **123,076** saved flights
- **42,214** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **123,076** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,487,725.8 tonnes** estimated CO2 emissions
- **86,244,972 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5035 |
| 2 | SkyWest Airlines | 4541 |
| 3 | EJA | 2386 |
| 4 | IndiGo | 2361 |
| 5 | American Airlines | 1900 |
| 6 | Southwest Airlines | 1844 |
| 7 | ENY | 1541 |
| 8 | Delta Air Lines | 1457 |
| 9 | Lufthansa | 1330 |
| 10 | LATAM Airlines | 1102 |
| 11 | Vueling | 1097 |
| 12 | WIF | 1091 |
| 13 | AZU | 1031 |
| 14 | AXM | 988 |
| 15 | LXJ | 946 |
| 16 | Swiss International | 868 |
| 17 | All Nippon Airways | 832 |
| 18 | Alaska Airlines | 803 |
| 19 | easyJet | 786 |
| 20 | QLK | 778 |
| 21 | EJU | 772 |
| 22 | Cathay Pacific | 689 |
| 23 | AEE | 682 |
| 24 | Air France | 675 |
| 25 | VIV | 669 |
| 26 | United Airlines | 659 |
| 27 | CXK | 652 |
| 28 | MXY | 644 |
| 29 | JetBlue | 620 |
| 30 | GLO | 615 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 104584 |
| 2 | 🇪🇸 ES | 8295 |
| 3 | 🇮🇳 IN | 7401 |
| 4 | 🇦🇺 AU | 7181 |
| 5 | 🇧🇷 BR | 6814 |
| 6 | 🇩🇪 DE | 6570 |
| 7 | 🇮🇹 IT | 6545 |
| 8 | 🇨🇦 CA | 6465 |
| 9 | 🇯🇵 JP | 5427 |
| 10 | 🇬🇧 GB | 5418 |
| 11 | 🇫🇷 FR | 4902 |
| 12 | 🇨🇴 CO | 4029 |
| 13 | 🇲🇽 MX | 3575 |
| 14 | 🇬🇷 GR | 3513 |
| 15 | 🇳🇴 NO | 3394 |
| 16 | 🇨🇭 CH | 3167 |
| 17 | 🇹🇷 TR | 2578 |
| 18 | 🇲🇾 MY | 2557 |
| 19 | 🇿🇦 ZA | 2041 |
| 20 | 🇵🇱 PL | 2023 |
| 21 | 🇳🇿 NZ | 1986 |
| 22 | 🇹🇭 TH | 1932 |
| 23 | 🇰🇷 KR | 1926 |
| 24 | 🇵🇭 PH | 1758 |
| 25 | 🇬🇹 GT | 1706 |
| 26 | 🇲🇦 MA | 1319 |
| 27 | 🇲🇪 ME | 1228 |
| 28 | 🇲🇴 MO | 1176 |
| 29 | 🇳🇱 NL | 1174 |
| 30 | 🇧🇸 BS | 1072 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2588 |
| 2 | Denver International Airport |  | US | 2062 |
| 3 | Tokyo International Airport |  | JP | 1797 |
| 4 | Indira Gandhi International Airport |  | IN | 1631 |
| 5 | Harry Reid International Airport |  | US | 1536 |
| 6 | Guaymaral Airport |  | CO | 1517 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1484 |
| 8 | Zurich Airport |  | CH | 1370 |
| 9 | La Aurora Airport |  | GT | 1317 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1307 |
| 11 | Frankfurt am Main International Airport |  | DE | 1284 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1207 |
| 13 | Chicago O'Hare International Airport |  | US | 1192 |
| 14 | Macau International Airport |  | MO | 1176 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1073 |
| 17 | Capua Airport |  | IT | 1053 |
| 18 | Madrid Barajas International Airport |  | ES | 1027 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1026 |
| 20 | Kuala Lumpur International Airport |  | MY | 993 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 973 |
| 22 | Congonhas Airport |  | BR | 957 |
| 23 | Charlotte/Douglas International Airport |  | US | 926 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 905 |
| 25 | Charles de Gaulle International Airport |  | FR | 903 |
| 26 | Bengaluru International Airport |  | IN | 889 |
| 27 | Malpensa International Airport |  | IT | 853 |
| 28 | Ninoy Aquino International Airport |  | PH | 815 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 807 |
| 30 | Daniel K Inouye International Airport |  | US | 787 |
| 31 | Barcelona International Airport |  | ES | 769 |
| 32 | Tenerife Norte Airport |  | ES | 764 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 748 |
| 34 | Calgary International Airport |  | CA | 723 |
| 35 | Vitoria/Foronda Airport |  | ES | 716 |
| 36 | Amsterdam Airport Schiphol |  | NL | 711 |
| 37 | Norman Y Mineta San Jose International Airport |  | US | 709 |
| 38 | Scottsdale Airport |  | US | 707 |
| 39 | Seattle-Tacoma International Airport |  | US | 704 |
| 40 | Don Mueang International Airport |  | TH | 698 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 632 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 446 | 21m | 244 km | 1,878.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 320 | 24m | 225 km | 1,241.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 310 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 296 | 1h 10m | 770 km | 3,932.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 294 | 1h 25m | 910 km | 4,613.5 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 240 | 26m | 275 km | 1,137.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 178 | 26m | 215 km | 659.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 175 | 20m | 99 km | 299.8 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 171 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 170 | 44m | 241 km | 706.1 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 168 | 27m | 152 km | 439.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 158 | 1h 44m | 1,423 km | 3,877.6 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 155 | 18m | 144 km | 385.6 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 151 | 20m | 250 km | 652.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 144 | 1h 38m | 1,156 km | 2,872.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 140 | 1h 17m | 961 km | 2,320.6 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 137 | 29m | 49 km | 115.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 137 | 13m | - | - |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PSGMM | PSG | Jundiai Airport (SBJD) | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | 2026-06-28 18:13 UTC | 2026-06-28 18:29 UTC | 15m |
| N622TP |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-06-28 17:59 UTC | 2026-06-28 18:26 UTC | 27m |
| N7040Q |  | Blairstown Airport (K1N7) | Blairstown Airport (K1N7) | 2026-06-28 17:53 UTC | 2026-06-28 18:26 UTC | 33m |
| VAR402 | VAR | Phoenix Goodyear Airport (KGYR) | Bishop Airfield (1AZ0) | 2026-06-28 17:54 UTC | 2026-06-28 18:20 UTC | 26m |
| N5115B |  | Auburn Municipal Airport (KAUN) | Sacramento Mather Airport (KMHR) | 2026-06-28 17:59 UTC | 2026-06-28 18:18 UTC | 19m |
| N1967S |  | Fullerton Municipal Airport (KFUL) | Riverside Airport (KRAL) | 2026-06-28 17:54 UTC | 2026-06-28 18:16 UTC | 22m |
| N4451P |  | Space Coast Regional Airport (KTIX) | Sapelo Island Airport (08GA) | 2026-06-28 16:34 UTC | 2026-06-28 18:16 UTC | 1h 42m |
| AAE127 | AAE | Henri Coanda International Airport (LROP) | Zhuhai Airport (ZGSD) | 2026-06-28 08:28 UTC | 2026-06-28 18:13 UTC | 9h 44m |
| LXJ446 | LXJ | Calgary International Airport (CYYC) | Calgary International Airport (CYYC) | 2026-06-28 17:54 UTC | 2026-06-28 18:07 UTC | 12m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-06-28 17:46 UTC | 2026-06-28 18:06 UTC | 19m |
| N885M |  | Bonaventure Airport (CYVB) | Dewitt Field/Old Town Municipal Airport (KOLD) | 2026-06-28 17:27 UTC | 2026-06-28 18:02 UTC | 35m |
| TKR105 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-06-28 17:28 UTC | 2026-06-28 18:00 UTC | 31m |
| N100LC |  | Casper/Natrona County International Airport (KCPR) | Infinity Landing Airport (SD25) | 2026-06-28 17:11 UTC | 2026-06-28 17:59 UTC | 47m |
| N135RF |  | Casas Adobes Airpark (NM69) | Casas Adobes Airpark (NM69) | 2026-06-28 17:47 UTC | 2026-06-28 17:57 UTC | 10m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-06-28 17:39 UTC | 2026-06-28 17:57 UTC | 18m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-06-28 17:38 UTC | 2026-06-28 17:55 UTC | 17m |
| N220BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-06-28 16:51 UTC | 2026-06-28 17:55 UTC | 1h 4m |
| HLE09 | HLE | RAF Ternhill (EGOE) | DCAE Cosford Airport (EGWC) | 2026-06-28 17:43 UTC | 2026-06-28 17:54 UTC | 11m |
| N525HS |  | Meadows Field (KBFL) | Truckee-Tahoe Airport (KTRK) | 2026-06-28 16:54 UTC | 2026-06-28 17:53 UTC | 59m |
| WIF9PM | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-28 17:04 UTC | 2026-06-28 17:52 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
