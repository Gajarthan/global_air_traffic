# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_11:42:56_UTC-green)

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

**Latest saved flight:** 2026-08-24 11:42:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 11:42:56 UTC

- **231,593** saved flights
- **71,282** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **231,593** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,792,889.0 tonnes** estimated CO2 emissions
- **161,906,608 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9303 |
| 2 | SkyWest Airlines | 8205 |
| 3 | EJA | 4472 |
| 4 | IndiGo | 3925 |
| 5 | American Airlines | 3786 |
| 6 | Southwest Airlines | 3574 |
| 7 | Delta Air Lines | 2958 |
| 8 | ENY | 2818 |
| 9 | LATAM Airlines | 2226 |
| 10 | AZU | 2148 |
| 11 | Vueling | 1976 |
| 12 | Lufthansa | 1884 |
| 13 | WIF | 1832 |
| 14 | LXJ | 1825 |
| 15 | easyJet | 1620 |
| 16 | Swiss International | 1551 |
| 17 | AXM | 1549 |
| 18 | EJU | 1479 |
| 19 | QLK | 1474 |
| 20 | United Airlines | 1471 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1385 |
| 23 | GLO | 1291 |
| 24 | WMT | 1279 |
| 25 | VIV | 1272 |
| 26 | PGT | 1265 |
| 27 | Air France | 1259 |
| 28 | Wizz Air | 1220 |
| 29 | AEE | 1154 |
| 30 | JetBlue | 1152 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192860 |
| 2 | 🇪🇸 ES | 14862 |
| 3 | 🇧🇷 BR | 13522 |
| 4 | 🇦🇺 AU | 13158 |
| 5 | 🇨🇦 CA | 12765 |
| 6 | 🇮🇹 IT | 12584 |
| 7 | 🇮🇳 IN | 12219 |
| 8 | 🇩🇪 DE | 11389 |
| 9 | 🇬🇧 GB | 10917 |
| 10 | 🇨🇴 CO | 9616 |
| 11 | 🇯🇵 JP | 9442 |
| 12 | 🇫🇷 FR | 9261 |
| 13 | 🇹🇷 TR | 6842 |
| 14 | 🇬🇷 GR | 6822 |
| 15 | 🇲🇽 MX | 6432 |
| 16 | 🇨🇭 CH | 6161 |
| 17 | 🇳🇴 NO | 5711 |
| 18 | 🇲🇾 MY | 4136 |
| 19 | 🇹🇭 TH | 4084 |
| 20 | 🇿🇦 ZA | 4047 |
| 21 | 🇵🇱 PL | 3843 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3184 |
| 24 | 🇬🇹 GT | 2903 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2663 |
| 27 | 🇲🇦 MA | 2351 |
| 28 | 🇲🇪 ME | 2129 |
| 29 | 🇳🇱 NL | 2070 |
| 30 | 🇮🇩 ID | 2010 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4820 |
| 2 | Denver International Airport |  | US | 3764 |
| 3 | Indira Gandhi International Airport |  | IN | 2826 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2493 |
| 7 | Zurich Airport |  | CH | 2419 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2363 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2330 |
| 10 | La Aurora Airport |  | GT | 2212 |
| 11 | El Dorado International Airport |  | CO | 2149 |
| 12 | Chicago O'Hare International Airport |  | US | 2096 |
| 13 | Salt Lake City International Airport |  | US | 2039 |
| 14 | Congonhas Airport |  | BR | 1973 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1958 |
| 16 | Frankfurt am Main International Airport |  | DE | 1849 |
| 17 | Capua Airport |  | IT | 1819 |
| 18 | Madrid Barajas International Airport |  | ES | 1818 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1738 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1719 |
| 21 | Malpensa International Airport |  | IT | 1661 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1656 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1608 |
| 25 | Macau International Airport |  | MO | 1603 |
| 26 | Ninoy Aquino International Airport |  | PH | 1533 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1495 |
| 29 | Barcelona International Airport |  | ES | 1456 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1400 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1374 |
| 33 | Bengaluru International Airport |  | IN | 1368 |
| 34 | Seattle-Tacoma International Airport |  | US | 1364 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1360 |
| 36 | Don Mueang International Airport |  | TH | 1335 |
| 37 | Calgary International Airport |  | CA | 1317 |
| 38 | Oslo Gardermoen Airport |  | NO | 1295 |
| 39 | O. R. Tambo International Airport |  | ZA | 1257 |
| 40 | Vitoria/Foronda Airport |  | ES | 1257 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 845 | 21m | 244 km | 3,558.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 563 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 382 | 27m | 275 km | 1,810.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 357 | 1h 50m | 1,423 km | 8,761.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 336 | 44m | 241 km | 1,395.7 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 12 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 324 | 44m | 555 km | 3,102.5 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 305 | 24m | 218 km | 1,149.1 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 300 | 1h 38m | 1,156 km | 5,984.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 281 | 27m | 215 km | 1,040.7 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 267 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 263 | 19m | 144 km | 654.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 250 | 15m | 154 km | 662.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EJU3737 | EJU | Malpensa International Airport (LIMC) | Ibiza Airport (LEIB) | 2026-08-24 09:53 UTC | 2026-08-24 11:42 UTC | 1h 49m |
| HBOCI | HBO | Birrfeld Airport (LSZF) | Fricktal-Schupfart Airport (LSZI) | 2026-08-24 11:11 UTC | 2026-08-24 11:41 UTC | 29m |
| GOODW | GOO | Fairoaks Airport (EGTF) | Fairoaks Airport (EGTF) | 2026-08-24 11:17 UTC | 2026-08-24 11:38 UTC | 21m |
| GYYRO | GYY | Tatenhill Airfield (EGBM) | DCAE Cosford Airport (EGWC) | 2026-08-24 11:21 UTC | 2026-08-24 11:38 UTC | 17m |
| DHXCF | DHX | Gelnhausen Airport (EDFG) | Wurzburg-Schenkenturm Airport (EDFW) | 2026-08-24 11:13 UTC | 2026-08-24 11:31 UTC | 17m |
| YOA | YOA | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-24 10:55 UTC | 2026-08-24 11:31 UTC | 35m |
| JANET33 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-08-24 11:17 UTC | 2026-08-24 11:29 UTC | 12m |
| N739PG |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-24 11:22 UTC | 2026-08-24 11:26 UTC | 3m |
| TSW1M | TSW | Nice-Cote d'Azur Airport (LFMN) | Hausen am Albis Airport (LSZN) | 2026-08-24 10:22 UTC | 2026-08-24 11:25 UTC | 1h 3m |
| RYR4YT | Ryanair | Vienna International Airport (LOWW) | Malpensa International Airport (LIMC) | 2026-08-24 10:13 UTC | 2026-08-24 11:25 UTC | 1h 11m |
| DEBFT | DEB | Gunzburg-Donauried Airport (EDMG) | Mengen-Hohentengen Airport (EDTM) | 2026-08-24 10:02 UTC | 2026-08-24 11:24 UTC | 1h 21m |
| GENBW | GEN | Lasham Airport (EGHL) | Lasham Airport (EGHL) | 2026-08-24 11:12 UTC | 2026-08-24 11:24 UTC | 12m |
| IBKUP | IBK | Voghera-Rivanazzano Airport (LILH) | Milano / Bresso Airport (LIMB) | 2026-08-24 10:54 UTC | 2026-08-24 11:23 UTC | 28m |
| RYR9EF | Ryanair | Francisco de Sá Carneiro Airport (LPPR) | Tannheim Airport (EDMT) | 2026-08-24 08:53 UTC | 2026-08-24 11:23 UTC | 2h 29m |
| RYR5603 | Ryanair | Kaunas International Airport (EYKA) | Wipperfurth-Neye Airport (EDKN) | 2026-08-24 09:29 UTC | 2026-08-24 11:22 UTC | 1h 53m |
| RYR838P | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Liege Airport (EBLG) | 2026-08-24 09:58 UTC | 2026-08-24 11:22 UTC | 1h 24m |
| N855MK |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-24 10:24 UTC | 2026-08-24 11:21 UTC | 57m |
| EAI64B | EAI | Dublin Airport (EIDW) | RAF Ternhill (EGOE) | 2026-08-24 10:21 UTC | 2026-08-24 11:17 UTC | 56m |
| PSDOR | PSD | Congonhas Airport (SBSP) | Clube do Ceu Airport (SDIN) | 2026-08-24 10:45 UTC | 2026-08-24 11:16 UTC | 30m |
| DLH2LN | Lufthansa | Frankfurt am Main International Airport (EDDF) | Ljubljana Joze Pucnik Airport (LJLJ) | 2026-08-24 10:16 UTC | 2026-08-24 11:13 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
