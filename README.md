# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_17:49:50_UTC-green)

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

**Latest saved flight:** 2026-09-22 17:49:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-22 17:49:50 UTC

- **266,466** saved flights
- **78,387** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **266,466** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,230,648.4 tonnes** estimated CO2 emissions
- **187,283,966 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10535 |
| 2 | SkyWest Airlines | 9267 |
| 3 | EJA | 5180 |
| 4 | IndiGo | 4474 |
| 5 | American Airlines | 4152 |
| 6 | Southwest Airlines | 3921 |
| 7 | Delta Air Lines | 3313 |
| 8 | ENY | 3134 |
| 9 | LATAM Airlines | 2568 |
| 10 | AZU | 2507 |
| 11 | Vueling | 2238 |
| 12 | WIF | 2160 |
| 13 | LXJ | 2094 |
| 14 | Lufthansa | 2039 |
| 15 | easyJet | 1791 |
| 16 | Swiss International | 1757 |
| 17 | QLK | 1721 |
| 18 | EJU | 1683 |
| 19 | AXM | 1667 |
| 20 | United Airlines | 1635 |
| 21 | Alaska Airlines | 1575 |
| 22 | All Nippon Airways | 1536 |
| 23 | PGT | 1503 |
| 24 | WMT | 1497 |
| 25 | GLO | 1487 |
| 26 | Air France | 1467 |
| 27 | VIV | 1459 |
| 28 | Wizz Air | 1449 |
| 29 | CXK | 1294 |
| 30 | AEE | 1285 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 221436 |
| 2 | 🇪🇸 ES | 16756 |
| 3 | 🇧🇷 BR | 15600 |
| 4 | 🇦🇺 AU | 15267 |
| 5 | 🇨🇦 CA | 14829 |
| 6 | 🇮🇹 IT | 14497 |
| 7 | 🇮🇳 IN | 14151 |
| 8 | 🇩🇪 DE | 12828 |
| 9 | 🇬🇧 GB | 12361 |
| 10 | 🇨🇴 CO | 12162 |
| 11 | 🇫🇷 FR | 10644 |
| 12 | 🇯🇵 JP | 10271 |
| 13 | 🇹🇷 TR | 8079 |
| 14 | 🇬🇷 GR | 7716 |
| 15 | 🇲🇽 MX | 7342 |
| 16 | 🇨🇭 CH | 7113 |
| 17 | 🇳🇴 NO | 6598 |
| 18 | 🇹🇭 TH | 4784 |
| 19 | 🇲🇾 MY | 4496 |
| 20 | 🇿🇦 ZA | 4470 |
| 21 | 🇵🇱 PL | 4380 |
| 22 | 🇳🇿 NZ | 3701 |
| 23 | 🇵🇭 PH | 3537 |
| 24 | 🇬🇹 GT | 3384 |
| 25 | 🇭🇷 HR | 3038 |
| 26 | 🇰🇷 KR | 3020 |
| 27 | 🇲🇦 MA | 2661 |
| 28 | 🇲🇪 ME | 2498 |
| 29 | 🇳🇱 NL | 2384 |
| 30 | 🇮🇩 ID | 2226 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5426 |
| 2 | Denver International Airport |  | US | 4326 |
| 3 | Indira Gandhi International Airport |  | IN | 3201 |
| 4 | Tokyo International Airport |  | JP | 3070 |
| 5 | El Dorado International Airport |  | CO | 2864 |
| 6 | Harry Reid International Airport |  | US | 2848 |
| 7 | Guaymaral Airport |  | CO | 2796 |
| 8 | Zurich Airport |  | CH | 2774 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2673 |
| 10 | La Aurora Airport |  | GT | 2570 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2568 |
| 12 | Salt Lake City International Airport |  | US | 2354 |
| 13 | Chicago O'Hare International Airport |  | US | 2290 |
| 14 | Congonhas Airport |  | BR | 2271 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2177 |
| 16 | Capua Airport |  | IT | 2084 |
| 17 | Madrid Barajas International Airport |  | ES | 2051 |
| 18 | Frankfurt am Main International Airport |  | DE | 2027 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2017 |
| 20 | Malpensa International Airport |  | IT | 1922 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1900 |
| 22 | Charles de Gaulle International Airport |  | FR | 1891 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1872 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1871 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1811 |
| 26 | Macau International Airport |  | MO | 1772 |
| 27 | Ninoy Aquino International Airport |  | PH | 1735 |
| 28 | Barcelona International Airport |  | ES | 1664 |
| 29 | Charlotte/Douglas International Airport |  | US | 1662 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1646 |
| 31 | Viracopos International Airport |  | BR | 1616 |
| 32 | Kuala Lumpur International Airport |  | MY | 1610 |
| 33 | Seattle-Tacoma International Airport |  | US | 1561 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1555 |
| 35 | Calgary International Airport |  | CA | 1520 |
| 36 | Don Mueang International Airport |  | TH | 1516 |
| 37 | Bengaluru International Airport |  | IN | 1507 |
| 38 | Oslo Gardermoen Airport |  | NO | 1501 |
| 39 | Vancouver International Airport |  | CA | 1490 |
| 40 | Antalya International Airport |  | TR | 1425 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1116 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 998 | 21m | 244 km | 4,202.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 739 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 669 | 1h 6m | 770 km | 8,887.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 663 | 24m | 225 km | 2,572.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 593 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 440 | 44m | 555 km | 4,213.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 424 | 1h 50m | 1,423 km | 10,405.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 405 | 44m | 241 km | 1,682.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 381 | 24m | 218 km | 1,435.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 362 | 21m | 250 km | 1,563.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 352 | 23m | 55 km | 334.6 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 340 | 12m | - | - |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 336 | 1h 6m | 706 km | 4,090.8 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 334 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 331 | 26m | 215 km | 1,225.9 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 310 | 19m | 144 km | 771.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 290 | 42m | 535 km | 2,678.3 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 279 | 18m | 14 km | 69.8 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CONGO63 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-09-22 17:31 UTC | 2026-09-22 17:49 UTC | 18m |
| BRG641 | BRG | Ralph Wien Memorial Airport (PAOT) | Deering Airport (PADE) | 2026-09-22 17:17 UTC | 2026-09-22 17:48 UTC | 30m |
| SCU59 | SCU | Sahoma Lake Airport (03OK) | Neversweat Airport (1OK0) | 2026-09-22 17:07 UTC | 2026-09-22 17:45 UTC | 38m |
| N9898M |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-09-22 16:47 UTC | 2026-09-22 17:34 UTC | 46m |
| ARCAS15 | ARC | Wichita Valley Airport (KF14) | 6TE2 (6TE2) | 2026-09-22 17:15 UTC | 2026-09-22 17:30 UTC | 14m |
| ARCAS16 | ARC | 4XA5 (4XA5) | 6TE2 (6TE2) | 2026-09-22 17:10 UTC | 2026-09-22 17:28 UTC | 17m |
| HARM31 | HAR | 4XA5 (4XA5) | 2XA0 (2XA0) | 2026-09-22 17:02 UTC | 2026-09-22 17:27 UTC | 24m |
| N846AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-09-22 16:39 UTC | 2026-09-22 17:26 UTC | 47m |
| LXJ510 | LXJ | Portsmouth International At Pease Airport (KPSM) | Hilton Head Airport (KHXD) | 2026-09-22 15:16 UTC | 2026-09-22 17:24 UTC | 2h 8m |
| CPA501 | Cathay Pacific | Narita International Airport (RJAA) | Chek Lap Kok International Airport (VHHH) | 2026-09-22 13:29 UTC | 2026-09-22 17:24 UTC | 3h 54m |
| FHHVP | FHH | Lyon-Bron Airport (LFLY) | Lyon Corbas Airport (LFHJ) | 2026-09-22 16:52 UTC | 2026-09-22 17:23 UTC | 31m |
| N9968F |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-09-22 16:51 UTC | 2026-09-22 17:22 UTC | 31m |
| N35597 |  | David Wayne Hooks Memorial Airport (KDWH) | Houston Executive Airport (KTME) | 2026-09-22 17:05 UTC | 2026-09-22 17:21 UTC | 15m |
| G72481 |  | Salt Lake City International Airport (KSLC) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-22 16:29 UTC | 2026-09-22 17:20 UTC | 50m |
| N129J |  | Chandler Municipal Airport (KCHD) | Montezuma Airport (19AZ) | 2026-09-22 16:51 UTC | 2026-09-22 17:20 UTC | 28m |
| N407LF |  | Skypark Airport (KBTF) | Skypark Airport (KBTF) | 2026-09-22 16:58 UTC | 2026-09-22 17:16 UTC | 17m |
| N230LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | 2026-09-22 15:34 UTC | 2026-09-22 17:16 UTC | 1h 41m |
| N481MR |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-09-22 16:22 UTC | 2026-09-22 17:15 UTC | 52m |
| THY6345 | Turkish Airlines | Istanbul Airport (LTFM) | Zhuhai Airport (ZGSD) | 2026-09-22 03:45 UTC | 2026-09-22 17:14 UTC | 13h 28m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-09-22 15:29 UTC | 2026-09-22 17:12 UTC | 1h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
