import { Divider, IconButton, Menu, MenuItem } from "@mui/material";
import { FC, MouseEvent, useState } from "react";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import { Model } from "@interfaces/common";
import useModelContext from "@context/ModelContext";
import AutoAwesomeMotionIcon from "@mui/icons-material/AutoAwesomeMotion";
import "./ModelsMenu.scss";

export const models: Model[] = [
  {
    set: "ETL_HIRAGANA",
    modelPath: "/kanji-recognizer/models/model_3_6.onnx",
    mapObjectPath: "/kanji-recognizer/models/model_3_6.json",
  },
  {
    set: "ETL_KATAKANA",
    modelPath: "/kanji-recognizer/models/model_3_10.onnx",
    mapObjectPath: "/kanji-recognizer/models/model_3_10.json",
  },
  {
    set: "ETL_KANJI",
    modelPath: "/kanji-recognizer/models/model_3_8.onnx",
    mapObjectPath: "/kanji-recognizer/models/model_3_8.json",
  },
  {
    set: "CUSTOM_HIRAGANA",
    modelPath: "/kanji-recognizer/models/model_3_3.onnx",
    mapObjectPath: "/kanji-recognizer/models/model_3_3.json",
  },
  {
    set: "CUSTOM_KATAKANA",
    modelPath: "/kanji-recognizer/models/model_2_6.onnx",
    mapObjectPath: "/kanji-recognizer/models/model_2_6.json",
  },
  {
    set: "CUSTOM_KANJI",
    modelPath: "/kanji-recognizer/models/model_3_11.onnx",
    mapObjectPath: "/kanji-recognizer/models/model_3_11.json",
  },
];

export const ModelsMenu: FC = () => {
  const [modelsMenuAnchor, setModelsMenuAnchor] = useState<null | HTMLElement>(
    null
  );
  const isModelsMenuOpen = Boolean(modelsMenuAnchor);
  const [selectedModel, setSelectedModel] = useState<string>(models[0].set);
  const { loadModel } = useModelContext();

  const handleOpen = (event: MouseEvent<HTMLElement>) =>
    setModelsMenuAnchor(event.currentTarget);

  const handleClose = () => setModelsMenuAnchor(null);

  const handleClick = async (model: Model) => {
    handleClose();
    setSelectedModel(model.set);
    await loadModel(model.modelPath, model.mapObjectPath);
  };
  return (
    <>
      <IconButton className="row--2" onClick={handleOpen}>
        {/* <MoreVertIcon sx={{ color: "#bfbfbf" }} /> */}
        <MoreVertIcon color="primary" />
      </IconButton>
      <Menu
        anchorEl={modelsMenuAnchor}
        open={isModelsMenuOpen}
        onClose={handleClose}
        sx={{ zIndex: (theme) => theme.zIndex.drawer }}
      >
        <MenuItem disabled>
          <AutoAwesomeMotionIcon />
          <span className="menu-item__label">SELECT MODEL</span>
        </MenuItem>
        <Divider />
        {models.map((model, index) => (
          <MenuItem
            key={index}
            selected={model.set === selectedModel}
            onClick={() => handleClick(model)}
          >
            <span className="menu-item__set">{model.set}</span>
          </MenuItem>
        ))}
      </Menu>
    </>
  );
};

export default ModelsMenu;
