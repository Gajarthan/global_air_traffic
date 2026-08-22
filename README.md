# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_11:49:18_UTC-green)

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

**Latest saved flight:** 2026-08-22 11:49:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 11:49:18 UTC

- **225,329** saved flights
- **70,141** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **225,329** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,715,619.1 tonnes** estimated CO2 emissions
- **157,427,194 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9037 |
| 2 | SkyWest Airlines | 7997 |
| 3 | EJA | 4353 |
| 4 | IndiGo | 3811 |
| 5 | American Airlines | 3705 |
| 6 | Southwest Airlines | 3524 |
| 7 | Delta Air Lines | 2879 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2143 |
| 10 | AZU | 2075 |
| 11 | Vueling | 1905 |
| 12 | Lufthansa | 1851 |
| 13 | WIF | 1791 |
| 14 | LXJ | 1777 |
| 15 | easyJet | 1561 |
| 16 | Swiss International | 1500 |
| 17 | AXM | 1491 |
| 18 | QLK | 1421 |
| 19 | EJU | 1419 |
| 20 | United Airlines | 1417 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1355 |
| 23 | GLO | 1245 |
| 24 | PGT | 1241 |
| 25 | VIV | 1231 |
| 26 | Air France | 1225 |
| 27 | WMT | 1209 |
| 28 | Wizz Air | 1166 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1122 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188755 |
| 2 | 🇪🇸 ES | 14442 |
| 3 | 🇧🇷 BR | 13065 |
| 4 | 🇦🇺 AU | 12776 |
| 5 | 🇨🇦 CA | 12480 |
| 6 | 🇮🇹 IT | 12069 |
| 7 | 🇮🇳 IN | 11884 |
| 8 | 🇩🇪 DE | 11101 |
| 9 | 🇬🇧 GB | 10582 |
| 10 | 🇨🇴 CO | 9258 |
| 11 | 🇯🇵 JP | 9180 |
| 12 | 🇫🇷 FR | 9004 |
| 13 | 🇹🇷 TR | 6596 |
| 14 | 🇬🇷 GR | 6579 |
| 15 | 🇲🇽 MX | 6259 |
| 16 | 🇨🇭 CH | 5944 |
| 17 | 🇳🇴 NO | 5578 |
| 18 | 🇲🇾 MY | 3971 |
| 19 | 🇿🇦 ZA | 3903 |
| 20 | 🇹🇭 TH | 3874 |
| 21 | 🇵🇱 PL | 3735 |
| 22 | 🇳🇿 NZ | 3138 |
| 23 | 🇵🇭 PH | 3077 |
| 24 | 🇬🇹 GT | 2850 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2535 |
| 27 | 🇲🇦 MA | 2263 |
| 28 | 🇲🇪 ME | 2016 |
| 29 | 🇳🇱 NL | 2012 |
| 30 | 🇮🇩 ID | 1945 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4706 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2743 |
| 4 | Indira Gandhi International Airport |  | IN | 2737 |
| 5 | Guaymaral Airport |  | CO | 2630 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2341 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2276 |
| 10 | La Aurora Airport |  | GT | 2172 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1911 |
| 16 | Frankfurt am Main International Airport |  | DE | 1816 |
| 17 | Madrid Barajas International Airport |  | ES | 1760 |
| 18 | Capua Airport |  | IT | 1734 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1678 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1668 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Macau International Airport |  | MO | 1593 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 24 | Malpensa International Airport |  | IT | 1587 |
| 25 | Charles de Gaulle International Airport |  | FR | 1560 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1471 |
| 28 | Kuala Lumpur International Airport |  | MY | 1443 |
| 29 | Barcelona International Airport |  | ES | 1394 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1368 |
| 31 | Bengaluru International Airport |  | IN | 1342 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1333 |
| 33 | Seattle-Tacoma International Airport |  | US | 1329 |
| 34 | Viracopos International Airport |  | BR | 1324 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1272 |
| 38 | Oslo Gardermoen Airport |  | NO | 1256 |
| 39 | Vitoria/Foronda Airport |  | ES | 1242 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1220 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 815 | 21m | 244 km | 3,431.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 562 | 1h 6m | 770 km | 7,465.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 354 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 338 | 1h 50m | 1,423 km | 8,295.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 327 | 44m | 241 km | 1,358.3 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 291 | 44m | 555 km | 2,786.5 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 286 | 1h 38m | 1,156 km | 5,705.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 283 | 24m | 218 km | 1,066.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 280 | 19m | 99 km | 479.6 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 257 | 19m | 144 km | 639.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KFS198 | KFS | Tweed/New Haven Airport (KHVN) | Tweed/New Haven Airport (KHVN) | 2026-08-22 11:35 UTC | 2026-08-22 11:49 UTC | 13m |
| GTI8782 | GTI | Ted Stevens Anchorage International Airport (PANC) | Miami International Airport (KMIA) | 2026-08-22 04:50 UTC | 2026-08-22 11:43 UTC | 6h 53m |
| GESGC | GES | Deanland Lewes Airport (EGKL) | Deanland Lewes Airport (EGKL) | 2026-08-22 10:40 UTC | 2026-08-22 11:37 UTC | 56m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 11:06 UTC | 2026-08-22 11:37 UTC | 30m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-22 08:41 UTC | 2026-08-22 11:25 UTC | 2h 44m |
| PH798 |  | Twenthe Airport (EHTW) | Twenthe Airport (EHTW) | 2026-08-22 09:57 UTC | 2026-08-22 11:25 UTC | 1h 28m |
| GSSCR | GSS | Fadmoor Airfield (EG19) | Fadmoor Airfield (EG19) | 2026-08-22 11:13 UTC | 2026-08-22 11:19 UTC | 5m |
| HBKBT | HBK | Langenthal Airport (LSPL) | Langenthal Airport (LSPL) | 2026-08-22 11:06 UTC | 2026-08-22 11:16 UTC | 10m |
| DFARO | DFA | Nevers-Fourchambault Airport (LFQG) | Nevers-Fourchambault Airport (LFQG) | 2026-08-22 10:43 UTC | 2026-08-22 11:14 UTC | 30m |
| N4431R |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-22 11:03 UTC | 2026-08-22 11:13 UTC | 10m |
| PH712 |  | Twenthe Airport (EHTW) | Twenthe Airport (EHTW) | 2026-08-22 11:03 UTC | 2026-08-22 11:09 UTC | 6m |
| IFJ16C | IFJ | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-08-22 11:01 UTC | 2026-08-22 11:05 UTC | 4m |
| AIQ3925 | AIQ | Don Mueang International Airport (VTBD) | Khunan Phumipol Airport (VTPY) | 2026-08-22 10:20 UTC | 2026-08-22 10:55 UTC | 35m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 10:42 UTC | 2026-08-22 10:54 UTC | 11m |
| VLG7HH | Vueling | Barcelona International Airport (LEBL) | Luqa Airport (LMML) | 2026-08-22 09:11 UTC | 2026-08-22 10:53 UTC | 1h 42m |
| EZY63FA | easyJet | Geneva Cointrin International Airport (LSGG) | London Luton Airport (EGGW) | 2026-08-22 09:23 UTC | 2026-08-22 10:52 UTC | 1h 29m |
| RRR4268 | RRR | MoD Boscombe Down Airport (EGDM) | Oslo Gardermoen Airport (ENGM) | 2026-08-22 08:44 UTC | 2026-08-22 10:50 UTC | 2h 5m |
| VLG6UA | Vueling | Barcelona International Airport (LEBL) | Menorca Airport (LEMH) | 2026-08-22 10:19 UTC | 2026-08-22 10:49 UTC | 30m |
| AIQ3074 | AIQ | Chiang Mai International Airport (VTCC) | Surat Thani Airport (VTSB) | 2026-08-22 09:25 UTC | 2026-08-22 10:49 UTC | 1h 23m |
| BGA123H | BGA | Saint-Nazaire-Montoir Airport (LFRZ) | Hamburg-Finkenwerder Airport (EDHI) | 2026-08-22 09:05 UTC | 2026-08-22 10:46 UTC | 1h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
